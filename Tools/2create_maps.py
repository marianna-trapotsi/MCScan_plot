import pandas as pd
import numpy as np
from tqdm import tqdm
import json
from Bio import SeqIO
from optparse import OptionParser
import os

parser=OptionParser()
parser.add_option('--directory_read', dest='dir_read', default=None, type=str, help='Select the directory, where the transcript.gtf and genome.fa files are stored')
parser.add_option('--directory_write', dest='dir_write', default=None, type=str, help='Select the directory where new files will be written')
#parser.add_option('--output_bed', dest='output_bed', default=None, type=str, help='Specify the directory and/or filename where the .bed file will be saved')
#parser.add_option('--output_fasta', dest='output_fa', default=None, type=str, help='Specify the directory and/or filename where the .cds.fa file will be saved')
#parser.add_option('--mappings', action='store_true', default=False, dest='maps', help='Set to save dictionary into  a json file')
parser.add_option('--log_error_id', action='store_true', default=False, dest='log_error', help='Set to save a text file with transcript ids that were not mapped to any gene id by using the gtf file')
parser.add_option('--species', dest='species', default=None, type=str, help='Select the species with the GHC subfolder where files are located')

(options, args)=parser.parse_args()

def introMessage():
    print('=======================================================================================================')
    print(' This script is converting the transcript ids into gene ids and overwrites fasta files with the gene id')
    print('=====================================================================================================\n')
    return()

def read_gtf(filename, output_file):
    file1=open(filename, 'r')
    Lines=file1.readlines()
    #Remove lines that start with # and are not data lines
    Lines=[x for x in Lines if x[0]!='#']    
    df=pd.DataFrame(Lines)[0].str.split('\t', expand=True)
    df=df[df[2].isin(['gene', 'CDS'])]

    cds=df[df[2]!='gene']
    genes=df[df[2]=='gene']

    cds_ids=cds[8].str.split(';', expand=True)
    gene_ids=genes[8].str.split(';', expand=True)
    file_bed=df[df[2]=='gene'][[0,3,4,7,6,8]].sort_values(0)
    gene_id=[]
    for i in file_bed[8]:
        for info in i.split(';'):
            if 'gene_id' in info:
                gene_id.append(info.split('gene_id'+' "')[1].split('"')[0])
            else:
                continue

    if len(gene_id)==file_bed.shape[0]:
        file_bed['gene_id']=gene_id
        print('Save Bed file')
        file_bed[[0,3,4,'gene_id',7,6]].to_csv(output_file, sep='\t', header=None, index=False)
    else:
        #file_bed[[0,3,4,'gene_id',7,6]].to_csv(output_file, sep='\t', header=None, index=False)
        print('Not all rows display the gene identifier - check the gtf or gff files')
    return(cds, genes, cds_ids, gene_ids)

def transcript_id_to_gene_id(cds_ids):
    transcript_to_gene={}
    transcript_no_genes=[]
    for transcript in tqdm(cds_ids[1].unique()):
        gene=cds_ids[cds_ids[1]==transcript][0].unique()
        if gene.shape[0]==0:
            transcript_no_genes.append(transcript.split(' "')[1].split('"')[0])
        else:
            for gene_row in gene:
                gene_name=gene_row.split(' "')[1].split('"')[0]
                transcript_to_gene[transcript.split(' "')[1].split('"')[0]]=gene_name
    return(transcript_to_gene, transcript_no_genes)

def rewrite_fasta(original_file, corrected_file, transcript_to_gene):
    with open(original_file) as original, open(corrected_file, 'w') as corrected:
        records = SeqIO.parse(original_file, 'fasta')
        for record in records:
            try:
                get_gene_id=transcript_to_gene[record.id]
                record.id=get_gene_id
                record.name=get_gene_id
                record.description=get_gene_id
                SeqIO.write(record, corrected, 'fasta')
            except:
                continue
    return(print('New corrected fasta created'))

if __name__=='__main__':
    introMessage()
    #Read GTF files and 1) create bed file and 2) prepare files for the rewrite_fasta function
    cds, genes, cds_ids, gene_ids=read_gtf(options.dir_read+'transcripts.gtf', options.dir_write+options.species+'.bed')
    
    command_var1='''awk '$3=="CDS"' ''' 
    os.system(command_var1 +options.dir_read+"transcripts.gtf > "+options.dir_write+"transcripts_onlycds.gtf")
    
    w_param=options.dir_write+options.species+'.transcripts.fa'
    x_param=options.dir_write+options.species+'_initial.cds.fa'
    y_param=options.dir_write+options.species+'.protein.fa'
    os.system('gffread -w ' + w_param+' -x ' + x_param + ' -y ' + y_param + ' -g ' + options.dir_read+'genome.fa '+ options.dir_write+'transcripts_onlycds.gtf -C')

    
    mappings, log_error_ids=transcript_id_to_gene_id(cds_ids)
   
    rewrite_fasta(options.dir_write+options.species+'_initial.cds.fa', options.dir_write+options.species+'.cds.fa', mappings)
    
    os.system("rm "+options.dir_write+"transcripts_onlycds.gtf")
    print('Run MCScan')
    os.system('python -m jcvi.formats.fasta format '+options.dir_write+options.species+'.cds.fa '+ options.dir_write+options.species+'.cds')
   

