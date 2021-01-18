import subprocess 
import argparse
import shutil
import sys
import time
from datetime import datetime
import re
import os.path
import pandas as pd
import sys

fixed_file = open("fixed_variants.txt", "w+")
fixed_file.write("Sample,Position,Protein,AAChange,NucleotideChange,AlleleFreq,Depth,Type,MatPeptide,MatPeptideAAChange,MatPeptideNucChange\n")

with open("variants.txt") as file1, open("visualization.csv") as file2:
    for line, line2 in zip(file1,file2):
        
        line_parts = line.split(",")
        fixed_aa_change = line_parts[1].split(" ")[1]
        fixed_protein = line_parts[1].split("#")[0] 
        if(line_parts[12].rstrip()=="-"):
            mat_peptide = ""
            mat_peptide_nuc_change = ""
            mat_peptide_aa_change = ""
        else:
            mat_peptide = line_parts[12].split(":")[0]
            mat_peptide_nuc_change = line_parts[12].split(":")[1].rstrip().split(";")[0].strip()
            mat_peptide_aa_change = line_parts[12].split(":")[1].rstrip().split(";")[1].strip()

        fixed_file.write(line_parts[0] + "," + line_parts[2] + "," + str(fixed_protein) + "," + str(fixed_aa_change) + "," + line_parts[6] + "," + str(line_parts[3]) + "," + str(line_parts[-1]) + "," + line_parts[8] + "," + mat_peptide + "," + mat_peptide_nuc_change + "," + mat_peptide_aa_change + "\n") 