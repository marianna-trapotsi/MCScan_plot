import pandas as pd
import numpy as np
from tqdm import tqdm
import json
from Bio import SeqIO
from optparse import OptionParser
import os

parser=OptionParser()
parser.add_option('--directory', dest='directory', default=None, type=str, help='Select the directory, where the individual species files are stored')
parser.add_option('--ref_directory', dest='ref_directory', default=None, type=str, help='Select the directory, where the individual species files are stored')
parser.add_option('--species', dest='species', default=None, type=str, help='Select the species with the GHC subfolder where files are located')
parser.add_option('--ref_species', dest='ref_species', default=None, type=str, help='Select the species with the GHC subfolder where files are located')
parser.add_option('--n_genes', dest='n_genes', default=20, type=int, help='Number of upstream and downstream genes from cluster')
(options, args)=parser.parse_args()

# Read Flam Coordinates
coordinates=pd.read_excel('../../Tools/220901_flam_coordinates.xlsx')
coordinates=coordinates.dropna(subset=['Species']).reset_index(drop=True)
coordinates=coordinates[coordinates['Unnamed: 11'].isin(['flam','flam','flam’'])].reset_index(drop=True)
coordinates['Strand']=np.where(coordinates['Strand']=='+', 'plus', 'minus')

#Create a Dictionary, where key is the species with the build id and the values are the coordinates for the flam 
build2coords={}
species2build={}
for row in coordinates.iterrows():
    if row[1]['Species'] not in species2build.keys():
        species2build[row[1]['Species']]=[row[1]['Build']]
    else:
        update_build_list=species2build[row[1]['Species']]+[row[1]['Build']]
        species2build[row[1]['Species']]=update_build_list


for row in coordinates.iterrows():
    build2coords[row[1]['Species']+'_'+row[1]['Build']]=[row[1]['Chromosome'],row[1]['Strand'],int(row[1]['Start']) ,int(row[1]['End'])]

print(build2coords)
if options.ref_species in build2coords.keys():
    print(options.ref_species)
    # Get information about flam cluster for the reference species
    
    chromosome=build2coords[options.ref_species][0]
    start=build2coords[options.ref_species][2]
    end=build2coords[options.ref_species][3]

    #Read Reference species bed file
    bed_dm=pd.read_csv(options.ref_directory+options.ref_species+'/'+options.ref_species+'.bed', sep='\t', header=None)
    
    #Select 20 genes upstream and downstream of flam
    in_flam=bed_dm[(bed_dm[0]==chromosome)&(bed_dm[1]>start)&(bed_dm[2]<end)]
    downstream=bed_dm[(bed_dm[0]==chromosome)&(bed_dm[1]<start)].sort_values(1).tail(options.n_genes)
    upstream=bed_dm[(bed_dm[0]==chromosome)&(bed_dm[1]>end)].sort_values(1).head(options.n_genes)
    downstream['location']='down'
    in_flam['location']='in'
    upstream['location']='up'
    focus_genes=pd.concat([downstream, in_flam, upstream]).reset_index(drop=True)
    focus_genes.head()
    focus_range=[i for i in range(focus_genes[1].min(),focus_genes[2].max()+1)]
    
    
    
    df_simple=pd.read_csv(options.ref_species+'.'+options.species+'.anchors.simple', sep='\t', header=None)
    chromosomes_1=[]
    chromosomes_2=[]
    start=[]
    end=[]
    for row in df_simple.iterrows():
        chromosomes_1.append(bed_dm[bed_dm[3]==row[1][0]].values[0][0])
        chromosomes_2.append(bed_dm[bed_dm[3]==row[1][1]].values[0][0])
        start.append(bed_dm[bed_dm[3]==row[1][0]].values[0][1])
        end.append(bed_dm[bed_dm[3]==row[1][1]].values[0][2])
        
    df_simple['chr1']=chromosomes_1
    df_simple['chr2']=chromosomes_2
    df_simple['start']=start
    df_simple['end']=end
    
    test=df_simple[(df_simple['chr2']==chromosome)]
    
    genes_add_color=[]
    for row in test.iterrows():
        row_range=[i for i in range(row[1]['start'],row[1]['end']+1)]
        if np.intersect1d(np.array(row_range), np.array(focus_range)).shape[0]==0:
            continue
        else:
            genes_add_color.append(row[1][0])
            
    for gene in list(set(genes_add_color)):
        df_simple=df_simple.replace(gene,'g*'+gene)
        
        
    df_simple[[0,1,2,3,4,5]].to_csv(options.ref_species+'.'+options.species+'.anchors.simple',sep='\t',index=False, header=None)
    
else:
    print('No flam in reference species')


