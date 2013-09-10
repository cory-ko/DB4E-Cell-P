#!/usr/bin/env python

from Bio import SeqIO
import sys
import os.path
import os

__author__ = """
Name: Soh Ishiguro
E-mail: t10078si@sfc.kei.ac.jp
"""

def clean_up():
    if os.path.isfile('data/CDS_annotation.tbl'):
        os.remove('data/CDS_annotation.tbl')
        
    if os.path.isfile('data/rRNA_annotation.tbl'):
        os.remove('data/rRNA_annotation.tbl')
                
    if os.path.isfile('data/tRNA_annotation_tbl'):
        os.remove('data/tRNA_annotation_tbl')
 
def generate_annotation_files(gbk_file):

    cds_f  = open('data/CDS_annotation.tbl', 'a')
    rrna_f = open('data/rRNA_annotation.tbl', 'a')
    trna_f = open('data/tRNA_annotation.tbl', 'a')

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

