# Dfic vs Dmel - Flam-like 1

### Step 1 Create a folder to run analysis with name 'Dfic_Dmel'  and add Dfic_GCF_018152265 in the file_species.txt
```
cd MCScan_plot
mkdir Dfic_Dmel
```
### Step 1: Prepare .bed and .cds files
```
cd MCScan_plot/Tools
python prepare_files.py --ref_species Dmel_dm6 --directory folder_with_saved_gtf_species_files/
```

```
cp ../Species/Dfic_GCF_018152265/Dfic_GCF_018152265.bed .
cp ../Species/Dfic_GCF_018152265/Dfic_GCF_018152265.cds .
cp ../Ref_Species/Dmel_dm6/Dmel_dm6.bed .
cp ../Ref_Species/Dmel_dm6/Dmel_dm6.cds .
cp ../Tools/run_block_comparison.sh .
```
Run the following command and define the reference species,  the location of the flamlike cluster (chromosome, start and end) and the name of the folder, e.g.:
```
bash run_block_comparison.sh Dfic_GCF_018152265 chr x y Dfic_Dmel
```

#### Delete last line in blocks file because the last gene is mapping to a gene very far and therefore the plot is loosing the focus in the flamlike region. This should be the following:

```
LOC108093425    FBgn0026255
```

```
python -m jcvi.graphics.synteny blocks Dfic_GCF_018152265_Dmel_dm6.bed  blocks.layout --glyphcolor=orthogroup --glyphstyle=arrow 

mv blocks.pdf Dfic_GCF_018152265.Dmel_dm6.blocks_updated.pdf
mv *.pdf plots/
```
