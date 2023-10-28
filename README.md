# MCScan_plot
This repository provides a set of tools (.py and .sh scripts) to automate the use of MCScan with Drosophila Species.

# If you are running MCScan_plot tools for first time follow the steps below, if not proceed to Step 4

### 1. MCScan tool should first be installed and also any additional packages should also be installed. Instructions can be found here for jcvi and LASTAL:

https://github.com/tanghaibao/jcvi

https://github.com/tanghaibao/jcvi/wiki/MCscan-(Python-version)#pairwise-synteny-search

### 2. Download MCScan_plot and make the following folders:
```
cd MCScan_plot
mkdir Species Ref_Species
```

#### After creating the folders the file structure should be:
```
MCSCan_plot/
├── Ref_Species
├── Species
└── Tools
   ├── .py scripts
   ├── .sh scripts
   ├── file_species.txt
   ├── gene_synteny.yml
   └── flam coordinates (.txt file)

```
#### Note: In MCScan_plot/Tools/run_block_comparison.sh and MCScan_plot/Tools/run_MCScan.sh, replace "folder_with_saved_gtf_species_files", with the folder path where you have saved .gtf files
### 3. Before running scripts, activate your conda environment
#### if you do not have one, use the gene_synteny.yml to create one:
```
conda env create -f gene_synteny.yml
pip install pandas
pip install tqdm
pip install Bio
pip install jcvi
```
### 4. Activate your conda environment
```
conda activate gene_synteny
```

### 5. Prepare input files
Prepare a files_species with a list of species that will compared to the reference species. See the 'Tools/file_species.txt' for reference. e.g. select Dsim_GCF_016746395 and Drho_GCF_018152115.
```
cd Tools
nano file_species.txt
```
### 6. Run the pywrapper.py, e.g. select Dyak_GCF_016746365 as reference species
```
python prepare_files.py --ref_species Dyak_GCF_016746365 --directory folder_with_saved_gtf_species_files/
```
This script is calling the 2create_maps.py script, which reads the transcripts.gtf files and create a .bed file and a .cds file with the transcript sequences

### 7. Run MCSCan with the following command
```
python run_MCScan.py --ref_species Dyak_GCF_016746365
```
### 8. Optional: Run generate_pdf.py to concatenate all plots in one .pdf file
```
python generate_pdf.py
```
Otherwise plots for each Species vs Reference species can be found, e.g. for Dsim_GCF_016746395:
```
MCScan_plot/Species/Dsim_GCF_016746395/plots
```
#### Types of Plots
1. Dot Plot
2. Histogram
3. Karyotype with all chromosomes/fragments
4. Karyotype with only the chromosomes/fragments which contain genes in both species and also with annotated the 20 up/downstream genes for species with flam

### If you do not want to run the automated version see the Detailed_Instructions.md
### For block plots (e.g. flamlike1) see the Block_Intstructions.md
