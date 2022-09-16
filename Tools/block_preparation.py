import pandas as pd
import numpy as np
from tqdm import tqdm
from optparse import OptionParser
import os

parser=OptionParser()
parser.add_option('--species_ref', dest='species_ref', default=None, type=str, help='Select the reference species')
parser.add_option('--species', dest='species', default=None, type=str, help='Select the species with the GHC subfolder where files are located')
parser.add_option('--flamlike_start', dest='flamlike_start', default=20, type=int, help='position of flamlike start')
parser.add_option('--flamlike_end', dest='flamlike_end', default=20, type=int, help='position of flamlike end')
parser.add_option('--n_genes', dest='n_genes', default=20, type=int, help='number of adjacent genes to the flamlike region')
parser.add_option('--chromosome_ref', dest='chromosome_ref', default=None, type=str, help='Chromosome on which flamlike is located')
parser.add_option('--chromosome_query', dest='chromosome_query', default=None, type=str, help='Chromosome with synteny')

(options, args)=parser.parse_args()

bed_dm=pd.read_csv(options.species_ref+'.bed', sep='\t', header=None)

#Select x genes upstream and downstream of flam
in_flam=bed_dm[(bed_dm[0]==options.chromosome_ref)&(bed_dm[1]>options.flamlike_start)&(bed_dm[2]<options.flamlike_end)]
downstream=bed_dm[(bed_dm[0]==options.chromosome_ref)&(bed_dm[1]<options.flamlike_start)].sort_values(1).tail(options.n_genes)
upstream=bed_dm[(bed_dm[0]==options.chromosome_ref)&(bed_dm[1]>options.flamlike_end)].sort_values(1).head(options.n_genes)
downstream['location']='down'
in_flam['location']='in'
upstream['location']='up'
focus_genes=pd.concat([downstream, in_flam, upstream]).reset_index(drop=True)
print(focus_genes)
focus_range=[i for i in range(focus_genes[1].min(),focus_genes[2].max()+1)]

print('Number of upstream genes selected: ', upstream.shape)
print('Number of downstream genes selected: ', downstream.shape)

#Read anchors.simple files
df_simple=pd.read_csv(options.species_ref+'.'+options.species+'.anchors.simple',  sep='\t', header=None)
chromosomes_1=[]
chromosomes_2=[]
start=[]
end=[]

min_value=focus_genes.head(1)[1].values[0]
max_value=focus_genes.tail(1)[1].values[0]

#Read blocks
blocks=pd.read_csv(options.species_ref+'.'+options.species+'.i1.blocks', sep='\t', header=None).rename(columns={0:'from',1:'to'})
merged=pd.merge(left=blocks, right=bed_dm, left_on='from', right_on=3)
blocks_subset=merged[merged[0]==options.chromosome_ref]
blocks_subset=blocks_subset[(blocks_subset[1]>=min_value)&(blocks_subset[2]<=max_value)][['from','to']]
blocks_subset.to_csv('blocks', sep='\t',header=None,index=None)



#Read combined bed file and keep only relevant chromosomes
combined_bed=pd.read_csv(options.species_ref+'_'+options.species+'.bed', sep='\t', header=None)
find_chr=blocks[blocks['from'].isin(focus_genes[3].tolist())]['to'].tolist()
get_chr=combined_bed[combined_bed[3].isin(find_chr)].groupby(0).count().sort_values(1, ascending=False).index[0]
combined_bed=combined_bed[combined_bed[0].isin([options.chromosome_ref,get_chr])]
combined_bed=pd.concat([combined_bed[combined_bed[0]==options.chromosome_ref],combined_bed[combined_bed[3].isin(blocks_subset['to'].tolist())]])

combined_bed.to_csv(options.species_ref+'_'+options.species+'.bed', sep='\t',index=None, header=None)

blocks_subset=blocks_subset[blocks_subset['to'].isin(combined_bed[3].tolist()+['.'])]
blocks_subset.to_csv('blocks', sep='\t',header=None,index=None)



os.system("sed -e 's/species1/'"+options.species_ref+"'/g' -e 's/species2/'"+options.species+"'/g' -e 's/chromosome1/'"+options.chromosome_ref+"'/g' -e 's/chromosome2/'"+get_chr+"'/g'  /mnt/scratchb/ghlab/marianna/gene_synteny_analysis/Dpse_flamlike2_comparisons/blocks_layout_ref>> blocks.layout")

