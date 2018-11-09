#!/bin/bash

# Script for concatenating all aligned, trimmed .fasta files into one single file (does not however, properly concatenate based on taxa-id, allows multiple entries)
cat *_trimmed.fasta > comb_conc.fasta