#!/usr/bin/env python

from Bio import SeqIO
import sys

__author__ = """
Name: Soh Ishiguro
E-mail: t10078si@sfc.kei.ac.jp
"""

if len(sys.argv) == 2:
    gbk_file = sys.argv[1]
else:
    raise SystemExit("[Usage] python" + __file__ + " <in.gbk>")


def main():    
    DEBUG = 0
    gene_count = 0

    handle = open(gbk_file, 'r')
    for record in SeqIO.parse(handle, 'genbank'):
        for feature in record.features:
            if feature.type == 'CDS' or feature.type == 'rRNA' or feature.type == 'tRNA':
            
                if not 'pseudo' in feature.qualifiers and 'gene' in feature.qualifiers:
                    gene_name = feature.qualifiers['gene'][0]
                    start = feature.location.start
                    end = feature.location.end
                    strand = int(feature.location.strand)
                    seq = record.seq[start:end]
                    feature = feature.type
                    
                    print "%s\t%s\t%s\t%s\t%s\t%s" % (gene_name, strand, start, end, feature, seq)
                
                    gene_count += 1
                
    if DEBUG:
        print "gene count: ", gene_count


if __name__ == '__main__':
    main()
    

            

