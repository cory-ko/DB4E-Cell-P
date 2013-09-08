#!/usr/bin/env python

__author__ = 'Kazuki Oshita <cory@g-language.org>'

import sys
sys.path.append('./lib')

from species import *

# for debugging, please set echo=True
engine = create_engine('sqlite:///db/ecell.db')

# create table to DB
metadata.create_all(engine)

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
