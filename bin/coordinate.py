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

    
def extract_seq(seq='', start='', end='', circular=True):
    
    '''
    Genomic coordinate(1-based)
    
    Argument :    sequence, start, end, circular(default:True)
    Return value: extracted sequence
    
    '''
    
    if not seq or not start or not end:
        raise ValueError

    length = len(seq)
    print seq

    def circular():
        
        '''
        For circular genomic coordinate
        '''

        if start > 0 and end > 0:
            return seq[start-1:end]

        elif start > 0 and end < 0:
            return seq[start-1:length-abs(end)]
            

    def linear():
        
        '''
        For lnear genomic coordinate.
        '''
        
        if start > 0 and end > 0:
            pass

        elif start > 0 and end < 0:
            pass
    
    if circular:
        print "Circular genome sequence: "
        print circular()
        
    elif not circular:
        print "Linear sequence: "
        print linear()
        
"""
    if start > 0 and end > 0:
        return seq[start-1:end]
        
    elif start > 0 and end < 0:
        pass
        
    elif start < 0 and end > 0:
        pass
        
    elif start < 0 and end < 0:
        pass
        
    elif start == 0 or end == 0:
        pass

"""


def main():
    seq = 'TCATTTAGCCTCTCCACTTTGAGCCTGCTGAAACAAGGTG' #40
    s = 2
    e = -3
    
    extract_seq(seq=seq, start=s, end=e, circular=True)

    
if __name__ == '__main__':
    main()
    
