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

    cds_f  = open('CDS_annotation.tbl', 'a')
    rrna_f = open('rRNA_annotation.tbl', 'a')
    trna_f = open('tRNA_annotation_tbl', 'a')


    handle = open(gbk_file, 'r')
    
    for record in SeqIO.parse(handle, 'genbank'):
        for feature in record.features:
            if feature.type == 'CDS':
                            
                if not 'pseudo' in feature.qualifiers and 'gene' in feature.qualifiers:
                    gene    = feature.qualifiers['gene'][0]
                    start   = feature.location.start
                    end     = feature.location.end
                    strand  = int(feature.location.strand)
                    seq     = record.seq[start:end]
                    feature = feature.type
                    
                    cds_f.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (gene, strand, start, end, feature, seq))
                
                    
            elif feature.type == 'rRNA':
                gene    = feature.qualifiers['gene'][0]
                start   = feature.location.start
                end     = feature.location.end
                strand  = int(feature.location.strand)
                seq     = record.seq[start:end]
                feature = feature.type
                    
                rrna_f.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (gene, strand, start, end, feature, seq))
                
            elif feature.type == 'tRNA':
                gene    = feature.qualifiers['gene'][0]
                start   = feature.location.start
                end     = feature.location.end
                strand  = int(feature.location.strand)
                seq     = record.seq[start:end]
                feature = feature.type

                trna_f.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (gene, strand, start, end, feature, seq))


if __name__ == '__main__':
    main()
    

            

