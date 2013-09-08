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


# Gene class
class Genes(Species):
    def __init__(self, name, strand, start, end, feature, sequence, operon):
        Species.__init__(self, name, strand, start, end, feature, sequence)
        self.operon = operon

# table definition (Genes table)
genes_table = Table('genes', metadata,
                    Column('id',       Integer, primary_key=True),
                    Column('name',     String),
                    Column('strand',   String),                      
                    Column('start',    Integer),
                    Column('end',      Integer),
                    Column('feature',  String),
                    Column('sequence', String),
                    sqlite_autoincrement=True
                )

# Gene class
class rRNA(Species):
    def __init__(self, name, strand, start, end, feature, sequence):
        Species.__init__(self, name, strand, start, end, feature, sequence)

# table definition (rRNA table)
rRNA_table = Table('rRna', metadata,
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
mapper(Genes,   genes_table)
