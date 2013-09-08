#!/usr/bin/env python

__author__ = 'Kazuki Oshita <cory@g-language.org>'

from sqlalchemy import *
from sqlalchemy.orm import mapper, sessionmaker

class Species(object):
    def __init__(self, name, strand, start, end, feature, sequence):
        self.name = name
        self.strand = strand
        self.start = start
        self.end = end
        self.feature = feature
        self.sequence = sequence

# Metadata entity collection
metadata = MetaData()

# for debugging, please set echo=True
engine = create_engine('sqlite:///db/ecell.db')

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

# create table to DB
metadata.create_all(engine)

# mapping python class to table
mapper(Species, species_table)

# create session object
Session = sessionmaker()
Session.configure(bind=engine)

# session start!
session = Session()

# data registration to sqlite3
with open("data/refSeq_data.tbl", "r") as f:
    for line in f:
        (name, strand, start, end, feature, sequence) = line[:-1].split("\t")
        obj = Species(name, strand, start, end, feature, sequence)
        session.add(obj)

# commit to database
session.commit()
