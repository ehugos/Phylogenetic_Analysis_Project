#!/usr/bin/env python

import sys
from Bio import SeqIO

# Script for removing all taxa defined in remove_list
def filter_taxa():
	# Defines in and outfiles as well as the remove_id set
	infile = sys.argv[1]
	remove_list = sys.argv[2]
	outfile = sys.argv[3]
	remove_id =  set([])
	
	# Opens and reads the file containing taxa to remove
	with open (remove_list, 'r') as remove_f:
		for line in remove_f:
			line = line.strip()
			# Removes the > as to match the taxa.id 
			remove_id.add(str(line).replace(">", ""))	
	with open(infile) as ori_fasta, open(outfile, 'w') as edited:
		taxas = SeqIO.parse(ori_fasta, 'fasta')
		# Checks all taxa if they match the remove_id set, if not, they are printed out
		for taxa in taxas:
			print(taxa.id)
			if taxa.id not in remove_id:
				SeqIO.write(taxa, edited, 'fasta')

if __name__ == '__main__':
    filter_taxa()