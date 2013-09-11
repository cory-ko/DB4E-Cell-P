#!/usr/bin/env python

from generator import genbank_generator
from generator import promoter_generator
from generator import terminator_generator
from registration import registration4db

class Db4ecellp:
    def __init__(self):
        pass

    def generate_files(self):
        genbank_generator.clean_up()
        genbank_generator.generate_annotation_files("data/NC_000913.gbk")
        promoter_generator.generate_annotation_files("local/RegulonDATADist_cleanup/promoter.txt")
        terminator_generator.generate_annotation_files("local/RegulonDATADist_cleanup/TerminatorSet.txt")
    
    def generate_db(self):
        registration4db.generate_db()
