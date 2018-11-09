#!/bin/bash

cat comb_conc.fasta | grep '^>' | sort | uniq -d >> unique_dict.txt