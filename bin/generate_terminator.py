import sys
import re

__author__ = """
Name: Satoshi Tamaki
E-mail: coela.st@gmail.com
"""

def main():
    """
This script generates the operon DB from TerminatorSet.txt,
input data was collected from web resource of the RegulonDB.(not from Web page)
http://regulondb.ccg.unam.mx/menu/download/datasets/files/TerminatorSet.txt

SYNOPSIS: python generate_terminator.py TerminatorSet.txt
OUTPUT : terminator_id strand start end type(terminator) sequence
Terminator information from
    """

    for line in open(sys.argv[1], 'r'):
        line = line.rstrip()
        if not re.match('^[#]',line) and re.match('^\S',line):
            lineArray = line.split("\t")
            print lineArray
            if lineArray[3] in "forward":
                print "\t".join([lineArray[0],"1",lineArray[1],lineArray[2],"terminator",lineArray[4] ])
            else:
                print "\t".join([lineArray[0],"-1",lineArray[1],lineArray[2],"terminator",lineArray[4] ])

if __name__ == '__main__':
    main()
