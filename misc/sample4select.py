#!/usr/bin/env python
# sample script to search from DB

__author__ = 'Kazuki Oshita <cory@g-language.org>'

from sqlalchemy import *
from sqlalchemy.orm import mapper, sessionmaker

# Species class
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

# Species table
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


# for debugging, please set echo=True
engine = create_engine('sqlite:///db/ecell.db')

# mapping python class to table
mapper(Species, species_table)

# create session object
Session = sessionmaker()
Session.configure(bind=engine)

# session start!
session = Session()

# get species which starts from 80866
for o in session.query(Species).filter_by(start = 80866):
    print o.sequence

# get IDs about all direct species
for o in session.query(Species).filter_by(strand = 1):
    print o.id
