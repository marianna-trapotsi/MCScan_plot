# Dpse: Gene HCS66_mgp01 on chrM had inverted start and end:
#start: 15693
#end: 262

import pandas as pd
import numpy as np

dpse=pd.read_csv('Dpse_GCF_009870125.bed', sep='\t', header=None)

for gene in dpse.iterrows():
    if gene[1][1]>gene[1][2]:
        print(gene)
        dpse.loc[gene[0]]=gene[1][[0,2,1,3,4,5]].tolist()
    else:
	continue


print("Save corrected Dpse_GCF_009870125.bed file")
dpse.to_csv('Dpse_GCF_009870125.bed', sep='\t', header=None, index=None)
