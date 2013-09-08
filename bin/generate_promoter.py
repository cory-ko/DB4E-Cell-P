# author : Satoshi Tamaki (coela@g-language.org)

import sys
import re

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

