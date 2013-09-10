#!/usr/bin/env python

__author__ = 'Kazuki Oshita <cory@g-language.org>'

import sys

from species import species

def generate_db():
    # for debugging, please set echo=True
    engine = species.create_engine('sqlite:///db/ecli.db',echo=True)

    # create table to DB
    species.metadata.create_all(engine)

    # create session object
    Session = species.sessionmaker()
    Session.configure(bind=engine)

    # session start!
    session = Session()

    # data registration to sqlite3

    with open("data/CDS_annotation.tbl", "r") as f:
        for line in f:
            (name, strand, start, end, feature, sequence) = line[:-1].split("\t")
            obj = species.CDS(name, strand, start, end, feature, sequence)
            session.add(obj)

    with open("data/rRNA_annotation.tbl", "r") as f:
        for line in f:
            (name, strand, start, end, feature, sequence) = line[:-1].split("\t")
            obj = species.rRNA(name, strand, start, end, feature, sequence)
            session.add(obj)

    with open("data/tRNA_annotation.tbl", "r") as f:
        for line in f:
            (name, strand, start, end, feature, sequence) = line[:-1].split("\t")
            obj = species.tRNA(name, strand, start, end, feature, sequence)
            session.add(obj)

    with open("data/promoter_annotation.tbl", "r") as f:
        for line in f:
            (name, strand, start, end, feature, sequence) = line[:-1].split("\t")
            obj = species.Promoter(name, strand, start, end, feature, sequence)
            session.add(obj)

    with open("data/terminator_annotation.tbl", "r") as f:
        for line in f:
            (name, strand, start, end, feature, sequence) = line[:-1].split("\t")
            obj = species.Terminator(name, strand, start, end, feature, sequence)
            session.add(obj)

    session.commit()
