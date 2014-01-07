#! /usr/bin/python
import sys

if len(sys.argv) < 2:
    print "Usage: python remove_orphans.py <file.fastq>"
    exit()

def printrec(rec):
    for line in rec:
        sys.stdout.write(line);

with open(sys.argv[1], 'r') as file:
    record = []
    for line in file:
        if len(record) == 4: # we have full fastq record
            if line[:-2] != record[0][:-2]:
                record = [] # orphan found. ignore.
        if len(record) == 8:
            printrec(record)
            record = []
    record[len(record):] = [line]
