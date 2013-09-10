#!/usr/bin/env python


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
        '''
        For circular genomic coordinate
        '''
        
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
        '''
        For lnear genomic coordinate.
        '''
        
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



def main():
    s = 'TCATTTAGCCTCTCCACTTTGAGCCTGCTGAAACAAGGTG'
    gc = GenomicCoordinate(start=30, end=200, seq=s, circular=False)
    print gc.retrieve_seq()

    
if __name__ == '__main__':
    main()
    
