#!/usr/bin/env python

import os
import sys

path = os.path.abspath(os.path.dirname(__file__)) + '/..'
sys.path.append(path)

from db4ecellp import db4ecellp

class DB4EcellpDemo(object):
    def __init__(self):
        pass

    def run(self):
        self.db4ecellp = db4ecellp.Db4ecellp()

        print "Generating files..."
        self.db4ecellp.generate_files()

        print "Gennerating DB..."
        self.db4ecellp.generate_db()
    
if __name__ == "__main__":
    
    print "Running the DB4 E-Cell P...."
    demo = DB4EcellpDemo()
    demo.run()

