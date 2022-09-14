# MCScan_plot
This repository provides a set of tools (.py and .sh scripts) in order to use MCScan with Drosophila Species.
# If you are running MCScan_plot tools for first time follow the steps below, if not proceed to Step 4

### 1. MCScan tool should first be installed and also any additional packages should also be installed. Instructions can be found here for jcvi and LASTAL:

https://github.com/tanghaibao/jcvi

https://github.com/tanghaibao/jcvi/wiki/MCscan-(Python-version)#pairwise-synteny-search

#### or I have saved the packages in :
```
/mnt/nas-data/ghlab1/group_folders/marianna/software/
```

### 2. Download MCScan_plot/Tools and make the following folfers:
```
mkdir Species Ref_Species
```

#### After creating the folders the file structure should be:
```
MCSCan_plot/
├── Ref_Species
├── Species
├── Tools
   ├── .py scripts
   ├── .sh scripts
   └── flam coordinates (.txt file)
└── gene_synteny.yml

```
### 3. Before running any scripts you need to activate your conda environment
#### if you do not have one, use the gene_synteny.yml to create one:
```
conda env create -f gene_synteny.yml

```
### 4. Activate your conda environment
```
conda activate gene_synteny
```

### 5. Prepare input files
```
cd Tools
nano file_species.txt
```
