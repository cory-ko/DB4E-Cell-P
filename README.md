Database project for E-Cell 4 P
===========
Install dependencies
-----------
pip install -r requeirements.txt

Required packages
-----------
see requirements.txt


Scripts
-----------
cleanup_regulondb_tsv.pl

How to generate SQLite DB
-----------
1. python bin/parse_gbk.py > data/refSeq_data.tbl
2. python bin/registration4db.py
