#!/usr/bin/env python

import sys
import string

__author__ = '''
Name: Soh Ishiguro
E-mail: t10078si@sfc.keio.ac.jp
'''

class GenomicCoordinate(object):

    def __init__(start, end, seq, circular):
        self.start = start
        self.end = end
        self.seq = seq
        self.circular = circular
        self.length = len(seq)

    def __circular(self):
        pass

    def __linear(self):
        
        '''
        For lnear genomic coordinate.
        '''
        
        if self.start > 0 and self.end > 0:
            return self.seq[self.start:self.seq]

        elif self.start > 0 and end > self.length:
            return self.seq[self.start:self.length]
            
        elif self.start > self.length:
            return ''

            
    def retrieve_seq(self):
        if self.circular:
            __circular()
            
        elif not self.circular:
            __linear()



        
def extract_seq(seq='', start='', end='', circular=True):
    
    '''
    Genomic coordinate(1-based).
    
    Argument :    sequence, start, end, circular(default:True)
    Return value: extracted sequence
    
    '''
    
    if not seq or not start or not end or start == 0 or end == 0:
        raise ValueError("Invalid data")

    length = len(seq)
    print "Original seq: " + seq

    
    def circular():
        
        '''
        For circular genomic coordinate
        '''

        if start > end:
            return seq[start-1:end]

        elif end < start:
            return seq[start:length % end ]
            
        elif start > 0 and end > 0:
            return seq[start-1:end]

        elif start > 0 and end < 0:
            return seq[start-1:length-abs(end)]

        elif start < 0 and end > 0:
            return seq[start-1:length-abs(end)]
            
        elif start < 0 and end < 0:
            return seq[length-abs(end):length-abs(start)]

        
    def linear():
        
        '''
        For lnear genomic coordinate.
        '''
        
        if start > 0 and end > 0:
            return seq[start:seq]

        elif start > 0 and end > length:
            return seq[start:length]
            
        elif start > length:
            return ''
                
    if circular:
        print "Circular genome sequence: ",
        print circular()
        
    elif not circular:
        print "Linear sequence: ",
        print linear()
        

def main():
    seq = 'TCATTTAGCCTCTCCACTTTGAGCCTGCTGAAACAAGGTG' #40
    s =  30
    e =  100
    
    print "start: %d, end: %d" %(s, e)
    extract_seq(seq=seq, start=s, end=e, circular=False)

    
if __name__ == '__main__':
    main()
    
