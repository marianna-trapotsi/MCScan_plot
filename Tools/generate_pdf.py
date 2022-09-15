import pandas as pd
import numpy as np
from tqdm import tqdm
import os
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileMerger

pdfs=[]
files_species=pd.read_csv('file_species.txt', sep='\t', header=None)[0].tolist()
files_species.sort()

# Karyotypes
pdfs=[]
path_dir='../Species/'
for file in tqdm(files_species):
    try:
        for pdf_file in os.listdir(path_dir+file+"/"+'plots/'):
            if 'karyotype' in pdf_file and 'color' not in pdf_file :
                
                pdfs.append(path_dir+file+"/"+'plots/'+pdf_file)
            else:
                continue
    except:
        print(file)
        
merger = PdfFileMerger()
pdfs=[ i for i in pdfs if '._DM'  not in i]
pdfs=[ i for i in pdfs if '._kary'  not in i]


for pdf in pdfs:
    try:
        merger.append(pdf)
        
    except:
        continue

merger.write("results_Karyotype.pdf")
merger.close()

# Karyotypes filtered and coloured for flam
pdfs=[]
for file in tqdm(files_species):
    try:
        for pdf_file in os.listdir(path_dir+file+"/"+'plots/'):
            if 'color_karyotype' in pdf_file :
                
                pdfs.append(path_dir+file+"/"+'plots/'+pdf_file)
            else:
                continue
    except:
        print(file)
        
merger = PdfFileMerger()
pdfs=[ i for i in pdfs if '._DM'  not in i]
pdfs=[ i for i in pdfs if '._kary'  not in i]


for pdf in pdfs:
    try:
        merger.append(pdf)
        
    except:
        continue

merger.write("results_ColoredKaryotype.pdf")
merger.close()

# Depth Histograms
pdfs=[]
for file in tqdm(files_species):
    try:
        for pdf_file in os.listdir(path_dir+file+"/"+'plots/'):
            if 'depth' in pdf_file:
                
                pdfs.append(path_dir+file+"/"+'plots/'+pdf_file)
            else:
                continue
    except:
        print(file)
        
merger = PdfFileMerger()
pdfs=[ i for i in pdfs if '._DM'  not in i]
pdfs=[ i for i in pdfs if '._kary'  not in i]


for pdf in pdfs:
    try:
        merger.append(pdf)
        
    except:
        continue

merger.write("results_Depth.pdf")
merger.close()



pdfs=[]
for file in tqdm(files_species):
    try:
        for pdf_file in os.listdir(path_dir+file+"/"+'plots/'):
            if 'depth' in pdf_file:
                continue
            elif 'karyotype'  in pdf_file:
                continue
                
                
            else:
                pdfs.append(path_dir+file+"/"+'plots/'+pdf_file)
    except:
        print(file)
        
merger = PdfFileMerger()
pdfs=[ i for i in pdfs if '._DM'  not in i]
pdfs=[ i for i in pdfs if '._kary'  not in i]


for pdf in pdfs:
    try:
        merger.append(pdf)
        
    except:
        continue

merger.write("results_DotPlot.pdf")
merger.close()


