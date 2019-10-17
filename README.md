**janitor** is a simple script that takes in a folder containing FASTA format files and verifies, for each 
file, if the sequences there contain all four nucleotides. It prints a report for all files that contain 
sequences of dubious quality (having absence of any nucleotide) with the IDs of the sequences.

Run **janitor** as:

    $ python3 janitor [path_to_folder] > janitor_log