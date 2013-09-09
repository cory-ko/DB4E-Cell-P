#!/usr/bin/env python

import sys
import string

__author__ = """
Name: Soh Ishiguro
E-mail: t10078si@sfc.keio.ac.jp
"""


def main():
    """
    This script generates the operon DB from OperonSet.txt,
    input data was collected from web resource of the RegulonDB.
    
    URL    : http://regulondb.ccg.unam.mx/menu/download/datasets/files/OperonSet.txt
    OUTPUT : promoter_name    start    end    strand    gene_name(s)
    
    """
    
    header = "%s\t%s\t%s\t%s\t%s" % ("promoter_id", "start", "end", "strand", "gene name(s)")
    print header

    file = '/home/soh.i/E-cell_Sprint/RegulonDATADist/OperonSet.txt'
    with open(file, 'r') as f:
        for line in f:
            
            if not line.startswith("#") and not line.isspace():
                data = line[:-1].split("\t")
                name = data[0]
                start = int(data[1])
                end  = int(data[2])
                strand = data[3]
                num_operon = int(data[4])
                gene_name = data[5]
                
                if 'forward' in strand:
                    strand = int(1)
                elif 'reverse' in strand:
                    strand = int(-1)
                
                print "%s\t%d\t%d\t%d\t%s" %(name, start, end, strand, gene_name)

                
if __name__ == '__main__':
    main()
    
                


                    

    
    
