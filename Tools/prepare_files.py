import os
import pandas as pd
import numpy as np
from tqdm import tqdm
from optparse import OptionParser

parser=OptionParser()
parser.add_option('--ref_species', dest='ref_species', default=None, type=str, help='Define the Reference species')
parser.add_option('--directory_read', dest='directory_read', default=None, type=str, help='Define the directory where species gtf files are saved')
(options, args)=parser.parse_args()

files=pd.read_csv('file_species.txt', sep='\t', header=None)[0].tolist()
for file in tqdm(files):
    species=file.split('_')[0]
    os.system('mkdir -p ../Species/' +file)
    directory_READ=options.directory_read+file.split('_')[0]+'/'+'_'.join(file.split('_')[1:])+'/'
    directory_WRITE='../Species/'+file+'/'

    os.system('sbatch prepare_files.sh '+file+' ' +directory_READ+' '+directory_WRITE)
    #print('bash prepare_files.sh '+file+' ' +directory_READ+' '+directory_WRITE)

for file in [options.ref_species]:
    os.system('mkdir -p ../Ref_Species/' +options.ref_species)
    directory_READ=options.directory_read+options.ref_species.split('_')[0]+'/'+'_'.join(options.ref_species.split('_')[1:])+'/'
    directory_WRITE='../Ref_Species/' +options.ref_species+'/'

    os.system('sbatch prepare_files.sh '+options.ref_species+' ' +directory_READ+' '+directory_WRITE)
    #print('bash prepare_files.sh '+options.ref_species+' ' +directory_READ+' '+directory_WRITE)
