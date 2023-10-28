# Instructions for flam synteny analysis between Dmel and Dbia and Dmel and Dele

### Step 1 Create a folder to run the first comparison with name 'Dmel_Dbia'  and add Dbia_GCF_018148935.bed and Dele_GCF_018152505 in the file_species.txt
```
cd MCScan_plot
mkdir Dmel_Dbia
cd Dmel_Dbia/
```
### Step 2: Prepare .bed and .cds files
```
cd MCScan_plot/Tools
python prepare_files.py --ref_species Dmel_dm6 --directory folder_with_saved_gtf_species_files/
```

```
cp ../Species/Dbia_GCF_018148935/Dbia_GCF_018148935.bed .
cp ../Species/Dbia_GCF_018148935/Dbia_GCF_018148935.cds .
cp ../Ref_Species/Dmel_dm6/Dmel_dm6.bed .
cp ../Ref_Species/Dmel_dm6/Dmel_dm6.cds .
cp ../Tools/run_block_comparison.sh .
```
Run the following command and define the reference species, and the location of the flamlike cluster (chromosome, start and end), e.g.:
```
bash run_block_comparison.sh Dmel_dm6 chr x y Dmel_Dbia
```

### Step 3: Create a folder to run the second comparison with name 'Dmel_Dele'
```
cd ../MCScan_plot
mkdir Dmel_Dele
cd Dmel_Dele/
```
```
cp ../Species/Dele_GCF_018152505/Dele_GCF_018152505.bed .
cp ../Species/Dele_GCF_018152505/Dele_GCF_018152505.cds .
cp ../Ref_Species/Dmel_dm6/Dmel_dm6.bed .
cp ../Ref_Species/Dmel_dm6/Dmel_dm6.cds .
cp ../Tools/run_block_comparison.sh .
```
Run the following command and define the reference species, and the location of the flamlike cluster (chromosome, start and end), e.g.:
```
bash run_block_comparison.sh Dmel_dm6 chr x y Dmel_Dele
```

### Step 4: Combine results in one plot
Make a new directory for the combined analysis
```
cd ../MCScan_plot/
mkdir Dmel_Dbia_Dele
cd Dmel_Dbia_Dele/
```
```
cp ../Dmel_Dbia/blocks blocks_Dmel_Dbia
cp ../Dmel_Dele/blocks blocks_Dmel_Dele

```

### Step 5: Combine the blocks files
```
python -m jcvi.formats.base join blocks_Dmel_Dbia blocks_Dmel_Dele --noheader | cut -f1,2,4,6 > blocks2
```

### Step 4: Copy bed files, combine them and create plot
Note: you need the blocks2.layout file, which is provided in this github folder.
```
cp ../Dmel_Dbia/Dmel_dm6.bed .
cp ../Dmel_Dele/Dele_GCF_018152505.bed .
cp ../Dmel_Dbia/Dbia_GCF_018148935.bed .

cat Dmel_dm6.bed Dbia_GCF_018148935.bed Dele_GCF_018152505.bed > Dmel_Dbia_Dele.bed
python -m jcvi.graphics.synteny blocks2 Dmel_Dbia_Dele.bed blocks2.layout --glyphcolor=orthogroup --glyphstyle=arrow
mv blocks2.pdf Dmel_Dbia_Dele_flam.pdf
```

