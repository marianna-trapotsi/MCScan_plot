# MCScan_plot
This repository provides a set of tools (.py and .sh scripts) in order to use MCScan with Drosophila Species.

#### 1. Can tool should first be installed and also any additional packages should also be installed. Instructions can be found here for jcvi and LASTAL:

https://github.com/tanghaibao/jcvi

https://github.com/tanghaibao/jcvi/wiki/MCscan-(Python-version)#pairwise-synteny-search

#### or I have saved the packages in :
```
/mnt/nas-data/ghlab1/group_folders/marianna/software/
```

#### Download MCScan_plot/Tools and make the following folfers:
```
mkdir Species Ref_Species
```

### After creating the folders the file structure should be:
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
### Before running an scripts you need to activate your conda environment
### if you do not have one, use the gene_synteny.yml to create one:
```
conda env create -f gene_synteny.yml
```

