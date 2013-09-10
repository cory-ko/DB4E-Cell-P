#!/usr/bin/env python

from Bio import SeqIO

__author__ = '''
Name: Soh Ishiguro
E-mail: t10078si@sfc.keio.ac.jp
'''


class GenomicCoordinateException(Exception):
    def __init__(self, start, end):
        self.start = start
        self.end   = end

    def __str__(self):
        return "Genomic position is only 1-based, given value of %d,%d value is not accepted." % (self.start, self.end)


class GenomicCoordinate(object):

    def __init__(self, start='', end='', seq='', circular=True):

        if circular:
            if start == 0 or end == 0:
                raise GenomicCoordinateException(start, end)
                
        elif not circular:
            if start <= 0 or end <= 0:
                raise GenomicCoordinateException(start, end)
        
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
    print "Extracted seq. \n%s\n" % (ss)
    
def linear_test():

    ecoli_genome = '../data/test.fa'
    
    ga = GenomicArray(ecoli_genome)	
    whole_seq_array = ga.seq_to_array()

    type1 = GenomicCoordinate(start=-1, end=0, seq=whole_seq_array, circular=True)
    print_seq(type1.retrieve_seq())

    #type2 = GenomicCoordinate(start=100, end=10000000, seq=whole_seq_array, circular=False)
    #print_seq(type2.retrieve_seq())

    #type3 = GenomicCoordinate(start=-1, end=0)
    #print_seq(type3.retrieve_seq())
    

def circular_genome():
    pass
    
    
if __name__ == '__main__':
    linear_test()
    
