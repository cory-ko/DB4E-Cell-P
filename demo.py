#-*- coding:utf-8 -*-

import os, sys

path = os.path.abspath(os.path.dirname(__file__)) + '/..'
sys.path.append(path)

from db4ecellp import db4ecellp

def main():
    _db4ecellp = db4ecellp.Db4ecellp()
    _db4ecellp.generate_files()
    _db4ecellp.generate_db()
    
if __name__ == "__main__":
    main()

