#!/bin/bash

# Rename all *.fasta.nex to *.nex
for f in *.nex; 
	do 
		mv -- "$f" "${f%.fasta.nex}.nex"
	done;