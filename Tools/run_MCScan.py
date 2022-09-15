import os
import pandas as pd
import numpy as np
from tqdm import tqdm
from optparse import OptionParser

parser=OptionParser()
#parser.add_option('--directory_read', dest='directory_read', default=None, type=str, help='Define the directory where species gtf files are saved')
parser.add_option('--ref_species', dest='ref_species', default=None, type=str, help='Select the Reference species')
(options, args)=parser.parse_args()

files=pd.read_csv('file_species.txt', sep='\t', header=None)[0].tolist()
for file in tqdm(files):
    os.system('sbatch run_MCScan.sh '+file+' '+options.ref_species)
   #print('sbatch run_MCScan.sh '+ file+ ' '+options.ref_species)            

