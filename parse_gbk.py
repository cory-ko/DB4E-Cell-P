#!/usr/bin/env python

from Bio import SeqIO
import sys

__author__ = """
Name: Soh Ishiguro
E-mail: t10078si@sfc.kei.ac.jp
"""

if len(sys.argv) == 2:
    gbk_file = sys.argv[1]
else:
    raise SystemExit("[Usage] python" + __file__ + " <in.gbk>")

handle = open(sys.argv[1])
for record in SeqIO.parse(handle, 'genbank'):
    #seq = str(record.seq)

    for feature in record.features:
        if feature.type == 'gene' or feature.type == 'rRNA' or feature.type == 'tRNA':
            if not 'pseudo' in feature.qualifiers:
                if 'gene' in feature.qualifiers:
                    gene_name = feature.qualifiers['gene'][0]
                    start = feature.location.start
                    end = feature.location.end
                    strand = feature.location.strand
                    print "%s\t%s\t%s\t%s" % (gene_name, strand, start, end)
                    

            

