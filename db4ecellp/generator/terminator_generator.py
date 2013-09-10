import sys
import re

__author__ = """
Name: Satoshi Tamaki
E-mail: coela.st@gmail.com
"""

"""
This script generates the operon DB from TerminatorSet.txt,
input data was collected from web resource of the RegulonDB.(not from Web page)
http://regulondb.ccg.unam.mx/menu/download/datasets/files/TerminatorSet.txt

SYNOPSIS: python generate_terminator.py TerminatorSet.txt
OUTPUT : terminator_id strand start end type(terminator) sequence
Terminator information from
"""

def generate_annotation_files(terminator_file):
    
    output_file = open('data/terminator_annotation.tbl','w');

    for line in open(terminator_file, 'r'):
        line = line.rstrip()
        if not re.match('^[#]',line) and re.match('^\S',line):
            lineArray = line.split("\t")
            if lineArray[3] in "forward":
                text =  "\t".join([lineArray[0],"1",lineArray[1],lineArray[2],"terminator",lineArray[4] ])
                output_file.write(text + "\n")
            else:
                text =  "\t".join([lineArray[0],"-1",lineArray[1],lineArray[2],"terminator",lineArray[4] ])
                output_file.write(text + "\n")

