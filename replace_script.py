# Script for replacing all instances of B in a fasta file with X
# To use this script, run: "python replace_script.py file_example.fasta"
# For multiple files, run: "python replace_script.py *.fasta" 
import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import re

for file_name in sys.argv[1:]:
	new_file_name = file_name.replace('.fasta','_rep.fasta')
	seq_list = []
	for fasta_seq in SeqIO.parse(file_name, 'fasta'):
		fasta_seq.seq = Seq(re.sub('[B]','[X]',str(fasta_seq.seq).upper()))
		seq_list.append(fasta_seq)
	with open(new_file_name, 'w') as handle:
		SeqIO.write(seq_list, handle, 'fasta')