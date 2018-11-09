#!/bin/bash

# Script for sequence trimming using trimAl, removes all gaps
# Gappyout removes gaps based on the gappyout algorithm
# -resoverlap and -seqoverlap removes sequences not achieving at least the stated % (i.e. spurious)
# ls *_al.fasta | parallel trimal -in {} -out {.}_trimmed.fasta -fasta -gappyout -resoverlap 0.75 -seqoverlap 80
 ls *_rep_al.fasta | parallel trimal -in {} -out {.}_trimmed.fasta -fasta -automated1