#!/usr/bin/env python

__author__ = 'Kazuki Oshita <cory@g-language.org>'

from sqlalchemy import *
from sqlalchemy.orm import mapper, sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)

# Metadata entity collection
metadata = MetaData()

# create table (gene)
species_table = Table('species', metadata,
                   Column('id',       Integer, primary_key=True),
                   Column('name',     String),
                   Column('feature',  String),
                   Column('start',    Integer),
                   Column('end',      Integer),
                   Column('sequence', String),
                   sqlite_autoincrement=True
               )

# create table
metadata.create_all(engine)

class Species(object):
    def __init__(self, name, feature, start, end, sequence):
        self.name = name
        self.feature = feature
        self.start = start
        self.end = end
        self.sequence = sequence

mapper(Species, species_table)

Session = sessionmaker()
Session.configure(bind=engine)

session = Session()


specie = Species('a', 'b', 1, 100, 'fdasfdsajfdslkj')



session.add(specie)

test_specie = session.query(Species).first()

print test_specie.id
