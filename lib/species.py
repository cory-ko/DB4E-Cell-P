#!/usr/bin/env python

__author__ = 'Kazuki Oshita <cory@g-language.org>'

from sqlalchemy import *
from sqlalchemy.orm import mapper, sessionmaker

# Metadata entity collection
metadata = MetaData()

# Species (base) class
class Species(object):
    def __init__(self, name, strand, start, end, feature, sequence):
        self.name = name
        self.strand = strand
        self.start = start
        self.end = end
        self.feature = feature
        self.sequence = sequence

# table definition (Species table)
species_table = Table('species', metadata,
                      Column('id',       Integer, primary_key=True),
                      Column('name',     String),
                      Column('strand',   String),                      
                      Column('start',    Integer),
                      Column('end',      Integer),
                      Column('feature',  String),
                      Column('sequence', String),
                      sqlite_autoincrement=True
                  )


# cds class
class CDS(Species):
    def __init__(self, name, strand, start, end, feature, sequence):
        Species.__init__(self, name, strand, start, end, feature, sequence)

# table definition (cds table)
cds_table = Table('cds', metadata,
                    Column('id',       Integer, primary_key=True),
                    Column('name',     String),
                    Column('strand',   String),                      
                    Column('start',    Integer),
                    Column('end',      Integer),
                    Column('feature',  String),
                    Column('sequence', String),
                    sqlite_autoincrement=True
                )

# rRNA class
class rRNA(Species):
    def __init__(self, name, strand, start, end, feature, sequence):
        Species.__init__(self, name, strand, start, end, feature, sequence)

# table definition (rRNA table)
rRNA_table = Table('rrna', metadata,
                   Column('id',       Integer, primary_key=True),
                   Column('name',     String),
                   Column('strand',   String),                      
                   Column('start',    Integer),
                   Column('end',      Integer),
                   Column('feature',  String),
                   Column('sequence', String),
                   sqlite_autoincrement=True
               )

# tRNA class
class tRNA(Species):
    def __init__(self, name, strand, start, end, feature, sequence):
        Species.__init__(self, name, strand, start, end, feature, sequence)

# table definition (tRNA table)
tRNA_table = Table('trna', metadata,
                   Column('id',       Integer, primary_key=True),
                   Column('name',     String),
                   Column('strand',   String),                      
                   Column('start',    Integer),
                   Column('end',      Integer),
                   Column('feature',  String),
                   Column('sequence', String),
                   sqlite_autoincrement=True
               )

# promoter class
class Promoter(Species):
    def __init__(self, name, strand, start, end, feature, sequence):
        Species.__init__(self, name, strand, start, end, feature, sequence)

# table definition (promoter table)
promoter_table = Table('promoter', metadata,
                   Column('id',       Integer, primary_key=True),
                   Column('name',     String),
                   Column('strand',   String),                      
                   Column('start',    Integer),
                   Column('end',      Integer),
                   Column('feature',  String),
                   Column('sequence', String),
                   sqlite_autoincrement=True
               )

# Terminator class
class Terminator(Species):
    def __init__(self, name, strand, start, end, feature, sequence):
        Species.__init__(self, name, strand, start, end, feature, sequence)

# table definition (promoter table)
terminator_table = Table('terminator', metadata,
                   Column('id',       Integer, primary_key=True),
                   Column('name',     String),
                   Column('strand',   String),                      
                   Column('start',    Integer),
                   Column('end',      Integer),
                   Column('feature',  String),
                   Column('sequence', String),
                   sqlite_autoincrement=True
               )



# mapping python class to table
mapper(Species, species_table)
mapper(CDS,   cds_table)
mapper(rRNA,   rRNA_table)
mapper(tRNA,   tRNA_table)
mapper(Promoter, promoter_table)
mapper(Terminator,   terminator_table)

