#! /usr/bin/python

import sys

from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

helpStr = "Usage: python check_blast.py <seq_file> <format>"

if len(sys.argv) < 3:
    print helpStr
    exit()

filePath   = sys.argv[1]
fileOption = sys.argv[2]

handle = open(filePath, "rU")

try:
    for record in SeqIO.parse(handle, fileOption):
        b = NCBIWWW.qblast("blastn", "nr", record.seq)
        blast_record = NCBIXML.read(b)

        E_VALUE_THRESH = 0.04

        alignment = blast_record.alignments[0]

        for hsp in alignment.hsps:
            print "Blasting " + alignment.title
            if hsp.expect < E_VALUE_THRESH:
                print '****Alignment****'
                print 'sequence:', alignment.title
                print 'e value:', hsp.expect
    handle.close()

except:
    print "There was a parsing issue."
    print "Make sure you have specified a file format and have internet access."
    print helpStr
