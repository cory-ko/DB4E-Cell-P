#!/usr/bine/env python

import sys
import string

from Bio import SeqIO

def to_array(seq):
    record = SeqIO.read(seq, "fasta")
    return [s for s in record]
    
ecoli_genome = '/home/soh.i/E-cell_Sprint/NC_000913.fna'
print to_array(ecoli_genome)


