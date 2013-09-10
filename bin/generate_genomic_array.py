#!/usr/bine/env python

import sys
import string

from Bio import SeqIO

def seq_to_array(seq):
    record = SeqIO.read(seq, "fasta")
    return [s for s in record]

def add_attribute_to_genomic_array():
    pass

    
ecoli_genome = '/home/soh.i/E-cell_Sprint/NC_000913.fna'
annotation_file = ''

with open(culated_file,'r') as f:
    for line in f:
        (gene, gene_start, gene_end, gene_strand) = line[:-1].split("\t")
        attribute = { gene: { "gene" : gene, "start" : start, "end" : end}}

        genomic_array = seq_to_array(ecoli_genome)
        for index, base enumerate in genomic_array:
            if gene_start <= base and gene_end >= base:
                genomic_array[index].append(attribute)


