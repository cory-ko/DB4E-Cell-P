Database project for E-Cell 4 P
===========

Required packages
-----------
see pip_requirements.txt

pip install -r requirement.txt

Scripts
-----------
cleanup_regulondb_tsv.pl

How to generate SQLite DB
-----------
1. python bin/parse_gbk.py > data/refSeq_data.tbl
2. python bin/registration4db.py
