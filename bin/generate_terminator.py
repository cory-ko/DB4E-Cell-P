# author : Satoshi Tamaki (coela@g-language.org)

import sys
import re

"""
Terminator information from
http://regulondb.ccg.unam.mx/menu/download/datasets/files/TerminatorSet.txt
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

