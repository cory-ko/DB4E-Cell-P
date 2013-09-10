# author : Satoshi Tamaki (coela@g-language.org)

import sys
import re
__author__ = """
Name: Satoshi Tamaki
E-mail: coela.st@gmail.com
"""

def main():
    """
This script generates the operon DB from promoter.txt,
input data was collected from web resource of the RegulonDB.(not from Web page)
SYNOPSIS: python generate_promoter.py promoter.txt
OUTPUT : promoter_id strand start end type(promoter) sequence
    """

    for line in open(sys.argv[1], 'r'):
        line = line.rstrip()
        if not re.match('^[#]',line):
            lineArray = line.split("\t")

            if not len(lineArray[3]):
                continue

            if lineArray[2] in "forward":
                print "\t".join([ lineArray[0],"1",lineArray[3],lineArray[3],"promoter",lineArray[9] ])
            else:
                print "\t".join([ lineArray[0],"-1",lineArray[3],lineArray[3],"promoter",lineArray[9] ])


if __name__ == '__main__':
    main()
