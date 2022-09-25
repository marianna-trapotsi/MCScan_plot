# Instructions for flam-like 2 synteny analysis between Dpse and Dper and Dpse and Dmir

### Step 1 Create a folder to run the first comparison with name 'Dpse_Dper'  and add Dper_GCF_003286085.bed and Dmir_GCF_003369915 in the file_species.txt
```
cd MCScan_plot
mkdir Dpse_Dper
cd Dpse_Dper/
```
### Step 2: Prepare .bed and .cds files
```
cd MCScan_plot/Tools
python prepare_files.py --ref_species Dpse_GCF_009870125 --directory /mnt/scratchb/ghlab/sus/REFERENCE/drosophila/species/
```

```
cp ../Species/Dper_GCF_003286085/Dper_GCF_003286085.bed .
cp ../Species/Dper_GCF_003286085/Dper_GCF_003286085.cds .
cp ../Ref_Species/Dpse_GCF_009870125/Dpse_GCF_009870125.bed .
cp ../Ref_Species/Dpse_GCF_009870125/Dpse_GCF_009870125.cds .
cp ../Tools/run_block_comparison.sh .
```
Run the following command and define the reference species, and the location of the flamlike cluster (chromosome, start and end), e.g.:
```
bash run_block_comparison.sh Dpse_GCF_009870125 chr x y Dpse_Dper
```

### Step 3: Create a folder to run the second comparison with name 'Dmel_Dele'
```
cd ../MCScan_plot
mkdir Dpse_Dmir
cd Dpse_Dmir/
```
```
cp ../Species/Dmir_GCF_003369915/Dmir_GCF_003369915.bed .
cp ../Species/Dmir_GCF_003369915/Dmir_GCF_003369915.cds .
cp ../Ref_Species/Dpse_GCF_009870125/Dpse_GCF_009870125.bed .
cp ../Ref_Species/Dpse_GCF_009870125/Dpse_GCF_009870125.cds .
cp ../Tools/run_block_comparison.sh .
```
Run the following command and define the reference species, and the location of the flamlike cluster (chromosome, start and end), e.g.:
```
bash run_block_comparison.sh Dmel_dm6 chr x y Dpse_Dmir
```

### Step 4: Combine results in one plot
Make a new directory for the combined analysis
```
cd ../MCScan_plot/
mkdir Dpse_Dper_Dmir
cd Dpse_Dper_Dmir/
```
```
cp ../Dpse_Dper/blocks blocks_Dpse_Dper
cp ../Dpse_Dmir/blocks blocks_Dpse_Dmir

```

### Step 5: Combine the blocks files
```
python -m jcvi.formats.base join blocks_Dpse_Dper blocks_Dpse_Dmir --noheader | cut -f1,2,4,6 > blocks2
```

### Step 4: Copy bed files, combine them and create plot
Note: you need the blocks2.layout file, which is provided in this github folder.
```
cp ../Dpse_Dper/Dpse_GCF_009870125.bed .
cp ../Dpse_Dper/Dper_GCF_003286085.bed .
cp ../Dpse_Dmir/Dmir_GCF_003369915.bed .

cat Dpse_GCF_009870125.bed Dper_GCF_003286085.bed Dmir_GCF_003369915.bed > Dpse_Dper_Dmir.bed
python -m jcvi.graphics.synteny blocks2 Dpse_Dper_Dmir.bed blocks2.layout --glyphcolor=orthogroup --glyphstyle=arrow
mv blocks2.pdf Dpse_Dper_Dmir_flamlike2.pdf
```

