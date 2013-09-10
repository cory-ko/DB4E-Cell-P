#!/usr/bin/env python

from Bio import SeqIO

__author__ = '''
Name: Soh Ishiguro
E-mail: t10078si@sfc.keio.ac.jp
'''

class GenomicCoordinate(object):

    def __init__(self, start='', end='', seq='', circular=True):
        self.start    = int(start)
        self.end      = int(end)
        self.sequence = seq
        self.circular = circular
        self.length   = len(seq)

    def get_circular_genome(self):
        
        """
        For circular genomic coordinate
        """
        
        if self.start > self.end:
            return self.sequence[self.start-1:self.end]

        elif self.end < self.start:
            return self.sequence[self.start:self.length % self.end]
            
        elif self.start > 0 and self.end > 0:
            return self.sequence[self.start-1:self.end]

        elif self.start > 0 and self.end < 0:
            return self.sequence[self.start-1:self.length-abs(self.end)]

        elif self.start < 0 and self.end > 0:
            return self.sequence[self.start-1:self.length-abs(self.end)]
            
        elif self.start < 0 and self.end < 0:
            return self.sequence[self.length-abs(end):self.length-abs(self.start)]


    def get_linear_genome(self):
        
        """
        For lnear genomic coordinate.
        """
        
        if self.start > 0 and self.end > 0:
            return self.sequence[self.start-1:self.end]

        elif self.start > 0 and self.end > self.length:
            return self.sequence[self.start-1:self.length]
            
        elif self.start > self.length:
            return ''

    def retrieve_seq(self):
        if self.circular:
            return self.get_circular_genome()
            
        elif not self.circular:
            return self.get_linear_genome()


class GenomicArray(object):
    
    """
    Generate whole genome sequence array per base.
    
    Argument: sequence file(fasta)
    Usage: gr = GenomicArray("in.fasta")
           gr.seq_to_array()
    Return value: [['A'], ['T'], ['G']...]
    """

    def __init__(self, seq):
        self.seq = seq
        
    def seq_to_array(self):
        record = SeqIO.read(self.seq, "fasta")
        self.rec = []
            
        for i in record.seq:
            self.rec.append([i])
        return self.rec


def print_seq(seq):
    
    print "Seq. length: %s" % (len(seq))

    ss = ''
    for s in seq:
        ss += s[0]
    print "Extracted seq. %s" % (ss)
    
    
def main():

    ecoli_genome = '../data/test.fa'
    ga = GenomicArray(ecoli_genome)	
    whole_seq_array = ga.seq_to_array()

    gc = GenomicCoordinate(start=30, end=200, seq=whole_seq_array, circular=False)
    
    print_seq(gc.retrieve_seq())
    
    
if __name__ == '__main__':
    main()
    
