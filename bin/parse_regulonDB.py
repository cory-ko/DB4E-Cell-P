#!/usr/bin/env python

import sys
import string
import re
import pprint

def main():
    sample_data = '/home/soh.i/E-cell_Sprint/RegulonDATADist/alignment.txt'
    
    selected = {}
    i = 0
    with open(sample_data) as fh:
        for line in fh:
            if not line.startswith("#"):
                itemList = line[:-1].split("\t")
                raise SystemExit("Error", itemList[3], SystemExit.code)
                                
                if "Translational" in itemList[2] and not "reverse" in itemList[3]:
                    key = "".join(itemList[0])
                                        
                    selected.update({key:{"ID" : itemList[1],
                                          "Annotation" : itemList[2],
                                          "Strand" : itemList[3]
                                       }})
            i += 1
                                    
    DEBUG = 0
    if DEBUG:
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(selected)

    for d in selected:
        print "%s\t%s\t%s" %(d, selected[d]["ID"], selected[d]["Strand"])

def toString(string):
    if isinstance(string, list):
        return "".join(string)
    else:
        return None

if __name__ == '__main__':
    main()
