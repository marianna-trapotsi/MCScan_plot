import pandas as pd
import numpy as np
from tqdm import tqdm
from optparse import OptionParser
import os

bed_dm=pd.read_csv('Dpse_GCF_009870125.bed', sep='\t', header=None)


n_genes=20
#Select x genes upstream and downstream of flam
in_flam=bed_dm[(bed_dm[0]=='chrX')&(bed_dm[1]>37962257)&(bed_dm[2]<38275576)]
downstream=bed_dm[(bed_dm[0]=='chrX')&(bed_dm[1]<37962257)].sort_values(1).tail(n_genes)
upstream=bed_dm[(bed_dm[0]=='chrX')&(bed_dm[1]>38275576)].sort_values(1).head(n_genes)
downstream['location']='down'
in_flam['location']='in'
upstream['location']='up'
focus_genes=pd.concat([downstream, in_flam, upstream]).reset_index(drop=True)
focus_range=[i for i in range(focus_genes[1].min(),focus_genes[2].max()+1)]
print('Number of upstream genes selected: ', upstream.shape)
print('Number of downstream genes selected: ', downstream.shape)


chromosomes_1=[]
chromosomes_2=[]
start=[]
end=[]

min_value=focus_genes.head(1)[1].values[0]
max_value=focus_genes.tail(1)[1].values[0]


#Read blocks


blocks=pd.read_csv('blocks2', sep='\t', header=None).rename(columns={0:'from',
                                                                              1:'to_Dper', 
                                                                              2:'to_Dmir'})
blocks.head()
merged=pd.merge(left=blocks, right=bed_dm, left_on='from', right_on=3)
merged.head()

blocks_subset=merged[merged[0]=='chrX']
blocks_subset.shape
blocks_subset=blocks_subset[(blocks_subset[1]>=min_value)&(blocks_subset[2]<=max_value)][['from','to_Dper', 'to_Dmir']]
blocks_subset.shape
blocks_subset.to_csv('blocks', sep='\t',header=None,index=None)



combined_bed=pd.read_csv('Dpse_Dper_Dmir.bed', sep='\t', header=None)


get_chrs=[]
for i in blocks_subset.columns:
    if i.startswith('to'):
        find_chr=blocks_subset[blocks_subset['from'].isin(focus_genes[3].tolist())][i].tolist()
        get_chr=combined_bed[combined_bed[3].isin(find_chr)].groupby(0).count().sort_values(1, ascending=False).index[0]
        print(get_chr)
        get_chrs.append(get_chr)


blocks_subset1=blocks_subset[blocks_subset['to_Dper'].isin(combined_bed[3].tolist()+['.'])]
blocks_subset2=blocks_subset[blocks_subset['to_Dmir'].isin(combined_bed[3].tolist()+['.'])]

blocks_subset=pd.concat([blocks_subset1,blocks_subset2]).drop_duplicates(keep='first')
blocks_subset[blocks_subset['from']!='flamlike'].to_csv('blocks', sep='\t',header=None,index=None)


get_block_lims=[i for i in blocks_subset['to_Dper'].tolist()+
                blocks_subset['to_Dmir'].tolist() if i!='.']

combined_bed=combined_bed[combined_bed[0].isin(['chrX']+get_chrs)]
keep_flamlike=combined_bed[combined_bed[3]=='flamlike']
combined_bed=pd.concat([keep_flamlike,combined_bed[(combined_bed[0]=='chrX')&(combined_bed[1]>=min_value)&(combined_bed[2]<=max_value)],combined_bed[combined_bed[3].isin(get_block_lims)]])

combined_bed.drop_duplicates(keep='first').to_csv('/mnt/scratchb/ghlab/marianna/MCScan_plot/Dpse_Dper_Dmir/Dpse_Dper_Dmir_processed.bed', sep='\t',index=None, header=None)
