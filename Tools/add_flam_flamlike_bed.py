import pandas as pd
import numpy as np
from optparse import OptionParser
import os

parser=OptionParser()
parser.add_option('--directory', dest='directory', default=None, type=str, help='Select the directory, where the bed files are stored')
(options, args)=parser.parse_args()

try:
    coordinates=pd.read_excel('../Tools/220901_flam_coordinates.xlsx')
except:
    coordinates=pd.read_excel('../../Tools/220901_flam_coordinates.xlsx')

coordinates_flamlike=coordinates.dropna(subset=['Species']).reset_index(drop=True)
coordinates_flamlike=coordinates_flamlike.dropna(subset=['Unnamed: 11'])
coordinates_flamlike=coordinates_flamlike[~coordinates_flamlike['Unnamed: 11'].isin(['flam','flam','flam’'])].reset_index(drop=True)
coordinates_flamlike=coordinates_flamlike.dropna(subset=['Chromosome'])
coordinates_flamlike['Strand']=np.where(coordinates_flamlike['Strand']=='+', 'plus', 'minus')

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

build2coords_flamlike={}
species2build_flamlike={}
for row in coordinates_flamlike.iterrows():
    if row[1]['Species'] not in species2build_flamlike.keys():
        species2build_flamlike[row[1]['Species']]=[row[1]['Build']]
    else:
        update_build_list=species2build_flamlike[row[1]['Species']]+[row[1]['Build']]
        species2build_flamlike[row[1]['Species']]=update_build_list


for row in coordinates.iterrows():
    build2coords[row[1]['Species']+'_'+row[1]['Build']]=[row[1]['Chromosome'],row[1]['Strand'],int(row[1]['Start']) ,int(row[1]['End'])]

for row in coordinates_flamlike.iterrows():
    build2coords_flamlike[row[1]['Species']+'_'+row[1]['Build']]=[row[1]['Chromosome'],row[1]['Strand'],int(row[1]['Start']) ,int(row[1]['End'])]



    
bed_files=os.listdir(options.directory)
bed_files=[i for i in bed_files if i.endswith('.bed')]

for bed_file in bed_files:
    print(bed_file)
    species_build=bed_file.split('.bed')[0]
    print(species_build)
    
    try:
        get_coordinates_flam=build2coords[species_build]
        get_coordinates_flam=[str(i) for i in get_coordinates_flam]
        if get_coordinates_flam[1]=='minus':
            get_coordinates_flam[1]='-'
        elif get_coordinates_flam[1]=='plus':
            get_coordinates_flam[1]='+'
        else:
            print('error')
            
            
        get_coordinates_flam=[get_coordinates_flam[0],get_coordinates_flam[2],get_coordinates_flam[3],'flam','.',get_coordinates_flam[1]]
        with open(options.directory+bed_file, 'a+') as outfile:
            outfile.write('\t'.join(get_coordinates_flam) +'\n')
   
        outfile.close()
    except:
        print('No flam')
    try:
        get_coordinates_flamlike=build2coords_flamlike[species_build]
        get_coordinates_flamlike=[str(i) for i in get_coordinates_flamlike]
        if get_coordinates_flamlike[1]=='minus':
            get_coordinates_flamlike[1]='-'
        elif get_coordinates_flamlike[1]=='plus':
            get_coordinates_flamlike[1]='+'
        else:
            print('error')
            
            
        get_coordinates_flamlike=[get_coordinates_flamlike[0],get_coordinates_flamlike[2],get_coordinates_flamlike[3],'flam-like','.',get_coordinates_flamlike[1]]
        with open(options.directory+bed_file, 'a+') as outfile:
            outfile.write('\t'.join(get_coordinates_flamlike) +'\n')
   
        outfile.close()
    except:
        print('No flamlike')
        

