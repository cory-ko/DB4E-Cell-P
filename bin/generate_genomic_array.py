#!/usr/bine/env python

from Bio import SeqIO


__author__ = """
Name: Soh Ishiguro
E-mail: t10078si@sfc.keio.ac.jp
"""

class GenomicArray(object):
    
    def __init__(self, seq):
        self.seq = seq
        
    def seq_to_array(self):
        
        """
        Generate whole genome sequence array per base.

        Argument: sequence file(fasta)
        
        Usage: gr = GenomicArray("in.fasta")
               gr.seq_to_array()
        
        Return value: [['A'], ['T'], ['G']...]
        
        """
    
        record = SeqIO.read(self.seq, "fasta")
        self.rec = []
        
        for i in record.seq:
            self.rec.append([i])

        return self.rec


ecoli_genome = '/home/soh.i/E-cell_Sprint/NC_000913.fna'
g = GenomicArray(ecoli_genome)
whole = g.seq_to_array()
print whole[0:10]


"""
annotation_file = '../data/CDS_annotation.tbl'

attribute = {}
with open(annotation_file,'r') as f:
    for line in f:
        (gene, gene_strand, gene_start, gene_end, feature, seq) = line[:-1].split("\t")
        attribute.update({ gene: { "gene" : gene, "start" : gene_start, "end" : gene_end, "strand" : gene_strand}})

genomic_array = seq_to_array(ecoli_genome)
print "generated genomic array"

#for index, base in enumerate(genomic_array):
for k in attribute:
    base = genomic_array[int(attribute[k]["start"])]
    genomic_array[int(attribute[k]["start"])].append(k)
                  
        
                   
 
print genomic_array


"""
