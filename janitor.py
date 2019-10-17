from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os
import argparse

parser = argparse.ArgumentParser(description="Finds non-typical proteing-coding gene sequences in FASTA files containing multiple genes.")
parser.add_argument("directory_path", metavar="N", type=str, help="The path to the directory containing the sequence files.")
args = parser.parse_args()

directory = os.fsencode(args.directory_path)
dirname = os.fsdecode(directory)

defectives = {}

for f in os.listdir(directory):
    filename = os.fsdecode(f)
    if filename.endswith('.fasta'):
        for gene in SeqIO.parse(dirname + filename, "fasta"):
            if ("A" not in gene) or ("C" not in gene) or ("T" not in gene) or ("G" not in gene):
                if not (filename in defectives.keys()):
                    defectives[filename] = []
                    defectives[filename].append(gene.id)              
                else:
                    defectives[filename].append(gene.id)              
    else:
        continue

for key in defectives:
    print("Report for {}:".format(key))
    for missing in defectives[key]:
        print(" > {} ---> Missing nucleotides".format(missing))
    print('')