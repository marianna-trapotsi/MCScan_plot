import pandas as pd
import numpy as np
from optparse import OptionParser
import os

parser=OptionParser()
parser.add_option('--directory', dest='directory', default=None, type=str, help='Select the directory, where the individual species files are stored')
parser.add_option('--ref_directory', dest='ref_directory', default=None, type=str, help='Select the directory, where the individual reference species files are stored')
parser.add_option('--ref_species', dest='ref_species', default=None, type=str, help='Define the Reference species')
parser.add_option('--species', dest='species', default=None, type=str, help='Select the species with the GHC subfolder where files are located')
(options, args)=parser.parse_args()

df=pd.read_csv(options.ref_directory+options.ref_species+'.bed', sep='\t', header=None)
dm_chromosomes=df[0].unique()

print("=============================================================")
print(options.directory+options.species+'.bed')
df1=pd.read_csv(options.directory+options.species+'.bed', sep='\t', header=None)
species_chromosomes=df1[0].unique()

with open(options.directory+'seqids', 'w+') as outfile:
    outfile.write(','.join(dm_chromosomes) +'\n')
    outfile.write(','.join(species_chromosomes))

outfile.close()




