# Detailed Instructions for MCScan_plot
Use this page if you want to run MCScan manually

### Step 1 - Follow Steps 1-6 from README.md
Following the steps above, you should have created the input files for the MCScan_plot, i.e.:
1. a .bed file
2. a .cds file

These files are created by running the 2create_maps.py script, which performs the following:
1. 
### Step 7: Go to the Species directory that you are going to compare with the Reference species. In this case, the Dyak_GCF_016746365 will be the reference species and the Dsim_GCF_016746395 the species that will be compared to the reference.
In that folder then copy the .bed and .cds files from the reference species, because MCSCan tool requires the files to be in the same folder.
```
cd MCScan_plot/Species/Dsim_GCF_016746395/ 
cp ../../Ref_Species/Dyak_GCF_016746365/Dyak_GCF_016746365.bed .
cp ../../Ref_Species/Dyak_GCF_016746365/Dyak_GCF_016746365.cds .
```

### Step 8: Perform Pairwise Synteny Search
Note: multiple files will be created do not delete them or move them because they will be used for the next steps
```
python -m jcvi.compara.catalog ortholog Dyak_GCF_016746365 Dsim_GCF_016746395 --no_strip_names
```

### Step 9: Pairwise Synteny Visualisation
This command will generate the Dot plot in .pdf
```
python -m jcvi.graphics.dotplot Dyak_GCF_016746365.Dsim_GCF_016746395.anchors
```

### Step 10: Synteny Pattern
This command will generate the syntenic depths in a histogram
```
python -m jcvi.compara.synteny depth --histogram Dyak_GCF_016746365.Dsim_GCF_016746395.anchors
```
### Step 11: Create seqids file
This file should include the name of chromosomes for each file
```
python ../../Tools/create_seqids.py --species Dsim_GCF_016746395 --ref_species Dyak_GCF_016746365 --ref_directory ../../Ref_Species/Dyak_GCF_016746365/ --directory ../../Species/Dsim_GCF_016746395/
```
For example, 
```
chr2L, chr2R, chr3L, chr3R, chr4, chrX
chr2L, chr2R, chr3L, chr3R, chr4, chrX
```

### Step 12: Prepare data for creating karyotype plot
```
python -m jcvi.compara.synteny screen --minspan=30 --simple Dyak_GCF_016746365.Dsim_GCF_016746395.anchors Dyak_GCF_016746365.Dsim_GCF_016746395.anchors.new
```




mkdir plots



