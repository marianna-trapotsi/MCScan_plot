import pandas as pd
import numpy as np
from optparse import OptionParser
import os
from tqdm import tqdm

parser=OptionParser()
parser.add_option('--directory', dest='directory', default=None, type=str, help='Select the directory, where the individual species files are stored')
parser.add_option('--species', dest='species', default=None, type=str, help='Select the species with the GHC subfolder where files are located')
parser.add_option('--ref_species', dest='ref_species', default=None, type=str, help='Define the Reference species')
parser.add_option('--gtf_directory', dest='gtf_directory', default=None, type=str, help='Select the directory, where the gtf files are stored')
(options, args)=parser.parse_args()


dm_chromosomes=[]
species_chromosomes=[]

print(options.directory+options.ref_species+'.'+options.species+'.anchors.new')
anchors_new=open(options.directory+options.ref_species+'.'+options.species+'.anchors.new','r')
anchor_lines=anchors_new.readlines()
anchor_lines=[i.split('\n')[0] for i in anchor_lines if i[0]!='#']
anchor_lines=pd.DataFrame(anchor_lines)[0].str.split('\t', expand=True)

var1=options.ref_species.split('_')[0]
var2=('_').join(options.ref_species.split('_')[1:])
gtf_dmel=open(options.gtf_directory+var1+'/'+var2+'/transcripts.gtf', 'r')

gtf_dmel=gtf_dmel.readlines()
gtf_dmel=[i.split('\n')[0] for i in gtf_dmel if i[0]!='#']
gtf_dmel=pd.DataFrame(gtf_dmel)[0].str.split('\t', expand=True)
gtf_dmel_gene=gtf_dmel[gtf_dmel[2]=='gene']


var1=options.species.split('_')[0]
var2=('_').join(options.species.split('_')[1:])
gtf=open(options.gtf_directory+var1+'/'+var2+'/transcripts.gtf', 'r')

gtf=gtf.readlines()
gtf=[i.split('\n')[0] for i in gtf if i[0]!='#']
gtf=pd.DataFrame(gtf)[0].str.split('\t', expand=True)
gtf_gene=gtf[gtf[2]=='gene']

species_chromosomes=[]
for geneid in tqdm(anchor_lines[1].unique()):
    chromosome_id=gtf_gene.loc[gtf_gene[8].str.contains(geneid, case=False)][0].values[0]
    if chromosome_id in species_chromosomes:
        continue
    else:
        species_chromosomes.append(chromosome_id)

dm_chromosomes=[]
for geneid in tqdm(anchor_lines[0].unique()):
    chromosome_id=gtf_dmel_gene.loc[gtf_dmel_gene[8].str.contains(geneid, case=False)][0].values[0]
    if chromosome_id in dm_chromosomes:
        continue
    else:
        dm_chromosomes.append(chromosome_id)


with open(options.directory+'seqids', 'w+') as outfile:
    outfile.write(','.join(dm_chromosomes) +'\n')
    outfile.write(','.join(species_chromosomes))

outfile.close()
