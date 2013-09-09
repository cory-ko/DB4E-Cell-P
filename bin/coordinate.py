#!/usr/bin/env python

import sys
import string

__author__ = '''
Name: Soh Ishiguro
E-mail: t10078si@sfc.keio.ac.jp
'''

def extract_seq(seq='', start='', end=''):
    '''
    Genomic coordinate(1-based)
    
    Argument :    sequence, start, end
    Return value: extracted sequence
    
    '''
    
    if not seq or not start or not end:
        raise ValueError

    length = len(seq)
    print seq
    
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
        
        

def main():
    seq = 'TCATTTAGCCTCTCCACTTTGAGCCTGCTGAAACAAGGTG' #40
    s = 1
    e = 3
    
    print extract_seq(seq=seq, start=s, end=e)

    
if __name__ == '__main__':
    main()
    
