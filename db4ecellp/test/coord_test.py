#!/usr/bin/env python

from coordinate import GenomicCoordinate
from coordinate import GenomicArray

import pytest

def test_genomic_coordinate():
    
    ecoli_genome = '/home/soh.i/E-cell_Sprint/NC_000913.fna'
    ga = GenomicArray(ecoli_genome)	
    whole_seq_array = ga.seq_to_array()

    gc = GenomicCoordinate(start=30, end=200, seq=whole_seq_array, circular=True)
    assert gc.retrieve_seq() == "ATGC"

test_genomic_coordinate()
    
