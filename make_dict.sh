#!/bin/bash

# Script for extracting all unique taxonomic identifiers from a .fasta file
cat comb_conc.fasta | grep '^>' | sort | uniq -d >> unique_dict.txt