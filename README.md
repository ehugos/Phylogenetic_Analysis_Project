# Phylogenetic_Analysis_Project
Repository for all code used in the Phylogenetic Analysis Project

align_script.sh is used for aligning .fasta files using MUSCLE, resulting in a .afa file

concatenate_script.sh is used for concatenating all specified data into a single file, does not however concatenate based on sequence-id.

convert_script.sh converts .fasta files to .nex files

generate_script.py generates a .fasta file, based on input, without taxa specied in a .txt file

make_dict.sh generates a .txt file for all unique taxonomic-id found in the input .fasta file

rename_script_nex.sh renames all .afa files to .fasta files

rename_script_nex.sh renames all .fasta.nex files to .nex files

replace_script.py replaces all instances of the character 'B' in a .fasta file sequence with the character 'X'

trim_script.sh uses the software TrimAl to trim .fasta input files using the setting automated1

The following RAxML-blackbox [1] settings were used on the Cipres Science gatway for 10 hours [2] for the purpose of maximum-likelihood analysis of the output-files generated from taxon jacknifing.

raxmlHPC-HYBRID -T 4 -s infile -N autoMRE -n result -f a -p 12345 -x 12345 -m PROTCATJTT 

[1] A. Stamatakis: "RAxML Version 8: A tool for Phylogenetic Analysis and Post-Analysis of Large Phylogenies". In Bioinformatics, 2014
[2] Miller, M.A., Pfeiffer, W., and Schwartz, T. (2010) "Creating the CIPRES Science Gateway for inference of large phylogenetic trees" in Proceedings of the Gateway Computing Environments Workshop (GCE), 14 Nov. 2010, New Orleans, LA pp 1 - 8.	 
