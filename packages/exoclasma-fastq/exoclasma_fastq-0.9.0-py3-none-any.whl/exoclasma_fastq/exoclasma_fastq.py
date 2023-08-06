__scriptname__ = 'exoclasma-fastq'
__version__ = 'v0.9.0'
__bugtracker__ = 'https://github.com/regnveig/exoclasma-fastq/issues'

from Bio import SeqIO #
from Bio.Seq import Seq #
from Bio.SeqRecord import SeqRecord #
import argparse
import bz2
import gzip
import json
import logging
import os
import subprocess
import sys
import tempfile


# -----=====| LOGGING |=====-----

logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.DEBUG)


# -----=====| DEPS |=====-----

def CheckDependency(Name):
	Shell = subprocess.Popen(Name, shell = True, executable = 'bash', stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	Stdout, _ = Shell.communicate()
	if Shell.returncode == 127:
		logging.error(f'Dependency "{Name}" is not found!')
		exit(1)
	if Shell.returncode == 126:
		logging.error(f'Dependency "{Name}" is not executable!')
		exit(1)

def CheckDependencies():
	CheckDependency('fastq-dump')


# ------======| SUBPROCESS |======------

def BashSubprocess(SuccessMessage, Command):
	logging.debug(f'Shell command: {Command}')
	Shell = subprocess.Popen(Command, shell = True, executable = 'bash', stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	_, Stderr = Shell.communicate()
	if (Shell.returncode != 0):
		logging.error(f'Shell command returned non-zero exit code {Shell.returncode}: {Command}\n{Stderr.decode("utf-8")}')
		exit(1)
	logging.info(SuccessMessage)


# -----=====| I/O |=====-----

def Open(FileName):
	GzipCheck = lambda FileName: open(FileName, 'rb').read(2).hex() == '1f8b'
	Bzip2Check = lambda FileName: open(FileName, 'rb').read(3).hex() == '425a68'
	CheckFlags = GzipCheck(FileName = FileName), Bzip2Check(FileName = FileName)
	OpenFunc = { (0, 1): bz2.open, (1, 0): gzip.open, (0, 0): open }[CheckFlags]
	return OpenFunc(FileName, 'rt')


# ------======| MISC |======------

def ArmorDoubleQuotes(String): return f'"{String}"'


# -----=====| COMMAND FUNC |=====-----

def FromMND(MNDFile, OutputFastQ, Compression):
	logging.info(f'{__scriptname__} FromMND {__version__}')
	CompressionFunc = { 'gzip': gzip.open, 'bz2': bz2.open, 'none': open }
	Strand = {'0': 'F', '16': 'R'}
	InputMND = Open(MNDFile)
	OutputR1 = CompressionFunc[Compression](OutputFastQ['R1'], 'wt')
	OutputR2 = CompressionFunc[Compression](OutputFastQ['R2'], 'wt')
	for Line in InputMND:
		SplitLine = Line.split(' ')
		AnnotationR1, AnnotationR2, PairAnnotation = dict(), dict(), dict()
		AnnotationR1['strand'], AnnotationR2['strand']  = str(Strand[SplitLine[0]]), str(Strand[SplitLine[4]])
		AnnotationR1['chr'], AnnotationR2['chr']  = str(SplitLine[1]), str(SplitLine[5])
		AnnotationR1['pos'], AnnotationR2['pos']  = int(SplitLine[2]), int(SplitLine[6])
		AnnotationR1['fragment'], AnnotationR2['fragment']  = int(SplitLine[3]), int(SplitLine[7])
		AnnotationR1['mapq'], AnnotationR2['mapq']  = int(SplitLine[8]), int(SplitLine[11])
		AnnotationR1['cigar'], AnnotationR2['cigar']  = str(SplitLine[9]), str(SplitLine[12])
		PairAnnotation['orientation']  = (AnnotationR1['strand'] + AnnotationR2['strand'])
		PairAnnotation['position'] = 'cis' if (AnnotationR1['chr'] == AnnotationR2['chr']) else 'trans'
		AnnotationJSON = json.dumps({ 'R1': AnnotationR1, 'R2': AnnotationR2, 'Pair': PairAnnotation }, separators=(',', ':'))
		SeqR1, SeqR2 = Seq(SplitLine[10]), Seq(SplitLine[13])
		QualityR1, QualityR2 = ([60] * len(SplitLine[10])), ([60] * len(SplitLine[13]))
		RecordR1 = SeqRecord(seq = SeqR1, id = str(SplitLine[14]), name = str(SplitLine[14]), description = AnnotationJSON, letter_annotations = {'phred_quality': QualityR1})
		RecordR2 = SeqRecord(seq = SeqR2, id = str(SplitLine[15]), name = str(SplitLine[15]), description = AnnotationJSON, letter_annotations = {'phred_quality': QualityR2})
		SeqIO.write([RecordR1], OutputR1, 'fastq')
		SeqIO.write([RecordR2], OutputR2, 'fastq')
	logging.info('Job finished')

def FromSRA(SRADataset, OutputFastQ):
	logging.info(f'{__scriptname__} FromSRA {__version__}')
	with tempfile.TemporaryDirectory() as TempDir:
		BaseName = os.path.basename(SRADataset)
		TempR1 = os.path.join(TempDir, f'{BaseName}_1.fastq')
		TempR1GZ = f'{TempR1}.gz'
		TempR2 = os.path.join(TempDir, f'{BaseName}_2.fastq')
		TempR2GZ = f'{TempR2}.gz'
		TempUnpaired = os.path.join(TempDir, f'{BaseName}.fastq')
		TempUnpairedGZ = f'{TempUnpaired}.gz'
		CommandFastQDump = ['set', '-o', 'pipefail', ';', 'mkfifo', ArmorDoubleQuotes(TempR1), ';', 'mkfifo', ArmorDoubleQuotes(TempR2), ';', 'mkfifo',  ArmorDoubleQuotes(TempUnpaired), ';', '(', 'cat', ArmorDoubleQuotes(TempR1), '|', 'gzip', '-c', '>', ArmorDoubleQuotes(TempR1GZ), ';', ')', '&', '(', 'cat', ArmorDoubleQuotes(TempR2), '|', 'gzip', '-c', '>', ArmorDoubleQuotes(TempR2GZ), ';', ')', '&', '(', 'cat', ArmorDoubleQuotes(TempUnpaired), '|', 'gzip', '-c', '>', ArmorDoubleQuotes(TempUnpairedGZ), ';', ')', '&', '(', 'fastq-dump', '--split-3', '-O', ArmorDoubleQuotes(TempDir), ArmorDoubleQuotes(SRADataset), ';', 'echo', '>', ArmorDoubleQuotes(TempR1), ';', 'echo', '>', ArmorDoubleQuotes(TempR2), ';', 'echo', '>', ArmorDoubleQuotes(TempUnpaired), ';', ')', ';', 'wait', ';']
		BashSubprocess('SraToFastq.FastQDump', ' '.join(CommandFastQDump))
		Result = {'R1': (TempR1GZ, OutputFastQ['R1']), 'R2': (TempR2GZ, OutputFastQ['R2']), 'Unpaired': (TempUnpairedGZ, OutputFastQ['U'])}
		for Index, File in Result.items():
			if os.path.exists(File[0]) and (os.path.getsize(File[0]) > 1024):
				CommandMove = ['mv', ArmorDoubleQuotes(File[0]), ArmorDoubleQuotes(File[1])]
				BashSubprocess(f'SraToFastq.Move.{Index}', ' '.join(CommandMove))
				Result[Index] = File[1]
			else: Result[Index] = None
		if (Result['R1'] is None) != (Result['R2'] is None):
			logging.error(RenderParameters('RuntimeError', 'SRA paired output is malformed!'))
			raise RuntimeError
		if (Result['R1'] is None) and (Result['R2'] is None) and (Result['Unpaired'] is None):
			logging.error(RenderParameters('RuntimeError', 'SRA output is empty!'))
			raise RuntimeError
	logging.info('Job finished')

# -----=====| PARSER |=====-----

def CreateParser():
	Parser = argparse.ArgumentParser(
		formatter_class = argparse.RawDescriptionHelpFormatter,
		description = f'{__scriptname__} {__version__}: Different file formats to Illumina-like FastQ',
		epilog = f'Bug tracker: {__bugtracker__}')

	Parser.add_argument('-v', '--version', action = 'version', version = __version__)
	Subparsers = Parser.add_subparsers(title = 'Commands', dest = 'command')

	FromMNDParser = Subparsers.add_parser('FromMND', help = f'FastQ from Juicer merged_nodups.txt file')
	FromMNDParser.add_argument('-M', required = True, type = str, help = f'merged_nodups.txt file. May be gzipped or bzipped')
	FromMNDParser.add_argument('-R1', required = True, type = str, help = f'Output FastQ R1')
	FromMNDParser.add_argument('-R2', required = True, type = str, help = f'Output FastQ R2')
	FromMNDParser.add_argument('-c', '--compression', type = str, default = 'gzip', help = f'Compression: gzip, bz2, none (default: gzip)')

	FromMNDParser = Subparsers.add_parser('FromSRA', help = f'FastQ from SRA Dataset')
	FromMNDParser.add_argument('-S', required = True, type = str, help = f'SRA Dataset. Access code or file. File is better.')
	FromMNDParser.add_argument('-R1', required = True, type = str, help = f'Output FastQ R1')
	FromMNDParser.add_argument('-R2', required = True, type = str, help = f'Output FastQ R2')
	FromMNDParser.add_argument('-U', required = True, type = str, help = f'Output FastQ Unpaired')
	return Parser


# -----=====| MAIN |=====-----

def main():
	Parser = CreateParser()
	Namespace = Parser.parse_args(sys.argv[1:])
	CheckDependencies()
	if Namespace.command == 'FromMND':
		merged_nodups = Namespace.M
		OutputFastQ = { 'R1': Namespace.R1, 'R2': Namespace.R2 }
		Compression = Namespace.compression
		FromMND(merged_nodups, OutputFastQ, Compression)
	elif Namespace.command == 'FromSRA':
		SRA = Namespace.S
		OutputFastQ = { 'R1': Namespace.R1, 'R2': Namespace.R2, 'U': Namespace.U }
		FromSRA(SRA, OutputFastQ)
	else: Parser.print_help()

if __name__ == '__main__': main()
