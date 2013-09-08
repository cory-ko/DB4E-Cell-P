import sys
import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation

gb_record = SeqIO.read(sys.argv[2], "genbank")

for line in open(sys.argv[1], 'r'):
		line = line.rstrip()
		if not re.match('^[#]',line):
				lineArray = line.split("\t")
				start = int(lineArray[3])
				string = lineArray[9]
				if lineArray[2] in "forward": 
						print (string.lower() ) in gb_record.seq[start - 61 : start + 20].lower()
				else:
						print string.lower() in gb_record.seq[start - 21 : start+60].reverse_complement().lower()
