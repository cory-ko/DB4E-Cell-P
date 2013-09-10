# author : Satoshi Tamaki (coela@g-language.org)

import sys
import re
__author__ = """
Name: Satoshi Tamaki
E-mail: coela.st@gmail.com
"""

"""
This script generates the operon DB from promoter.txt,
input data was collected from web resource of the RegulonDB.(not from Web page)
SYNOPSIS: python generate_promoter.py promoter.txt
OUTPUT : promoter_id strand start end type(promoter) sequence
"""

def generate_annotation_files(promoter_file):

    output_file = open('data/promoter_annotation.tbl','w');

    for line in open(promoter_file, 'r'):
        line = line.rstrip()
        if not re.match('^[#]',line):
            lineArray = line.split("\t")

            if not len(lineArray[3]):
                continue

            if lineArray[2] in "forward":
                text = "\t".join([ lineArray[0],"1",lineArray[3],lineArray[3],"promoter",lineArray[9] ])
                output_file.write(text + "\n")

            else:
                text =  "\t".join([ lineArray[0],"-1",lineArray[3],lineArray[3],"promoter",lineArray[9] ])
                output_file.write(text + "\n")

