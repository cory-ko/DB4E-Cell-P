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

    def circular(self):
        pass

    def linear(self):
        
        '''
        For lnear genomic coordinate.
        '''
        
        if self.start > 0 and self.end > 0:
            return self.sequence[self.start:self.length]

        elif self.start > 0 and self.end > self.length:
            return self.sequence[self.start:self.length]
            
        elif self.start > self.length:
            return ''

            
    def retrieve_seq(self):
        if self.circular:
            circular()

        elif not self.circular:
            linear()



s = 'TCATTTAGCCTCTCCACTTTGAGCCTGCTGAAACAAGGTG'
gc = GenomicCoordinate(start=10, end=20, seq=s, circular=False)
print gc.linear()


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
    pass
    #seq = 'TCATTTAGCCTCTCCACTTTGAGCCTGCTGAAACAAGGTG' #40
    #ss =  30
    #ee =  100
    
    #print "start: %d, end: %d" %(ss, ee)
    #extract_seq(seq=seq, start=ss, end=ee, circular=False)

    
if __name__ == '__main__':
    main()
    
