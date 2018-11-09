#!/bin/bash

# Uses the program seqmagick to convert .fasta files to nexus format
# Used in an attempt for concatenating trimmed sequences in .nex format as .fasta based methods failed, not used after supervisor concatenated files

for file in *_trimmed.fasta; 
	do 
		seqmagick convert --output-format nexus --alphabet protein "$file" "$file".nex
	done;