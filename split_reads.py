#! /usr/bin/python
import sys

if len(sys.argv) < 2:
    print "Usage: python split_reads.py <file.fastq>\nRequires .fastq as input."

reads1 = open(sys.argv[1] + ".1", "w")
reads2 = open(sys.argv[1] + ".2", "w")

def printrec(rec, r1, r2):
	cur = rec
	if cur[0][len(cur[0]) - 2:] == "1\n":
		for line in rec:
			r1.write(line);
	else:
		for line in rec:
			r2.write(line);


with open(sys.argv[1], 'r') as file:
	record = []
	for line in file:
		record[len(record):] = [line]
		if len(record) == 4:
			printrec(record, reads1, reads2)
			record = []
