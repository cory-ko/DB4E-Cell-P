#!/usr/bin/env python

import sys
from Bio import SeqIO
import pprint

__author__ = '''
Name: Soh Ishiguro
E-mail: t10078si@sfc.kei.ac.jp
'''

def main():
    """
    This script is used for generating promoter information per gene

    DATA URL: http://regulondb.ccg.unam.mx/menu/download/datasets/files/OperonSet.txt
    OUTPUT  : gene_name    strand    operon_id
    
    """
    file = '/home/soh.i/E-cell_Sprint/RegulonDATADist/OperonSet.txt'

    DEBUG = 0

    integrated_data = {}
    with open(file, 'r') as f:
        for line in f:
        
            if not line.startswith("#") and not line.isspace():
                data = line[:-1].split("\t")
            
                operon_name = 'OPERON_' + data[0]
                start       = int(data[1])
                end         = int(data[2])
                strand      = data[3]
                num_operon  = int(data[4])
                gene_names  = data[5]
            
                if 'forward' in strand:
                    strand = int(1)
                elif 'reverse' in strand:
                    strand = int(-1)
                
                gene = gene_names.split(",")
                for g in gene:
                    integrated_data.update({g : {'operon_id' : operon_name, 'strand' : strand}})


    if not DEBUG:
        for k in integrated_data:
            print "%s\t%d\t%s" % (k, integrated_data[k]['strand'], integrated_data[k]['operon_id'])
    else:
        pp = pprint.PrettyPrinter(depth=6)
        pp.pprint(integrate)
        

if __name__ == '__main__':
    main()
    
                

