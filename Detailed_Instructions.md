# Detailed Instructions for MCScan_plot
Use this page if you want to run MCScan step by step

### Step 1 - Follow Steps 1-6 from README.md
Following the steps above, you should have created the input files for the MCScan_plot, i.e.:
1. a .bed file
2. a .cds file

for each of the 2 species 
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

### Step 13 (Optional): Remove any chromosomes/fragments that do not map between the two species
This step can be used in cases of very fragmented assemblies, where a lot of fragments contain genes that do not map to the reference species' genome
```
python ../../Tools/create_seqids_subset_chrom.py --species Dsim_GCF_016746395 --directory ../../Species/Dsim_GCF_016746395/ --ref_species Dyak_GCF_016746365 --gtf_directory folder_with_saved_gtf_species_files
```

### Step 14: Create a 'layout' file, which is used as an instruction set to plot the karyotype in the following step
```
sed -e 's/species1/Dyak_GCF_016746365/g' -e 's/species2/Dsim_GCF_016746395/g' ../../Tools/layout_ref>> layout
```

### Step 15: Make karyotype plot and rename karyotype file
```
python -m jcvi.graphics.karyotype seqids layout
mv karyotype.pdf Dyak_GCF_016746365_Dsim_GCF_016746395_karyotype.pdf
```

### Step 16 (Optional): Add color to highlight a particular synteny block in the karyotype and Make karyotype plot
For this step you will need to use a coordinates file that contains the information of e.g. a unistrand flam-like cluster for the reference species
```
python ../../Tools/add_color_karyotype.py --species Dsim_GCF_016746395 --directory ../Species/Dsim_GCF_016746395/ --ref_species Dyak_GCF_016746365 --ref_directory ../../Ref_Species/
python -m jcvi.graphics.karyotype seqids layout
mv karyotype.pdf Dyak_GCF_016746365_Dsim_GCF_016746395_color_karyotype.pdf
```

### Step 17: Move all pdf files in the plots folder and remove the reference species .bed and .cds files that have been copied in Step 7
```
mkdir plots
mv *.pdf plots
rm Dyak_GCF_016746365.bed
rm Dyak_GCF_016746365.cds
```
