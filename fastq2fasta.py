#! /usr/bin/python

import sys

if len(sys.argv) < 2:
    print "Usage: python fastq2fasta.py <seq.fastq>"
    exit()

with open(sys.argv[1]) as file:
    linecount = 0
    for line in file:
        if linecount % 4 == 0 or linecount == 0:
            sys.stdout.write(line)
        if linecount % 4 == 1:
            sys.stdout.write('>' + line[1:])
        linecount = linecount + 1
