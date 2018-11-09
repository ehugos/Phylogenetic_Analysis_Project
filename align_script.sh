#!/bin/bash

# Script for parallel sequence alignment using MUSCLE
ls *_rep.fasta | parallel  muscle -in {} -out {.}.afa
