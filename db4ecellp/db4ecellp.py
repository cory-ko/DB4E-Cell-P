#!/usr/bin/env python

from generator import genbank_generator
from generator import promoter_generator
from generator import terminator_generator
from registration import registration4db
import os.path

__author__ = """
yukke(Soh Ishiguro, t10078si@sfc.keio.ac.jp),
coela(Satoshi Tamaki, coela.st@gmail.com)
"""


class Db4ecellpExcption(Exception):
    
    def __init__(self, file):
        self.required_file = file

    def __str__(self):
        return "%s is not found under the data/*" % (self.required_file)

        
class Db4ecellp(object):
    
    def __init__(self):
        gbk    = 'data/NC_000913.gbk'
        fna    = 'data/test.fa'
        prom   = 'data/PromoterSet.txt'
        termin = 'data/TerminatorSet.txt'
        
        if not os.path.isfile(gbk): 
            raise Db4ecellpExcption(gbk)
            
        if not os.path.isfile(fna):
            raise Db4ecellpExcption(fna)
            
        if not os.path.isfile(prom):
            raise Db4ecellpExcption(prom)
            
        if not os.path.isfile(termin):
            raise Db4ecellpExcption(termin)

        regulonDB_files = {
            "Genbank"        : gbk,
            "GenomeSequence" : fna,
            "Promoter"       : prom,
            "TerminatorSet"  : termin
        }
        
        self.regulonDB_files = regulonDB_files
        
    def generate_files(self):
        genbank_generator.clean_up()
        genbank_generator.generate_annotation_files(self.regulonDB_files["Genbank"])
        promoter_generator.generate_annotation_files(self.regulonDB_files["Promoter"])
        terminator_generator.generate_annotation_files(self.regulonDB_files["TerminatorSet"])
    
    def generate_db(self):
        registration4db.generate_db()
