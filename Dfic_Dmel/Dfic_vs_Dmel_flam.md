# Dfic vs Dmel - Flam-like 1
These are the instructions to generate Figure x.y 

### Step 1 Create a folder to run analysis with name 'Dfic_Dmel' 
```
cd MCScan_plot
mkdir Dfic_Dmel
cd Dfic_Dmel
```
### Step 1: Prepare .bed and .cds files
```
cd MCScan_plot/Tools
python prepare_files.py --ref_species Dmel_dm6 --directory /mnt/scratchb/ghlab/sus/REFERENCE/drosophila/species/
```

```
cp ../Species/Dfic_GCF_018152265/Dfic_GCF_018152265.bed .
cp ../Species/Dfic_GCF_018152265/Dfic_GCF_018152265.cds .
cp ../Ref_Species/Dmel_dm6/Dmel_dm6.bed .
cp ../Ref_Species/Dmel_dm6/Dmel_dm6.cds .
cp ../Tools/run_block_comparison .
```
Define the reference species, and the location of the flamlike cluster (chromosome, start and end)
```
bash run_block_comparison.sh Dfic_GCF_018152265 chrUn_025064569 438589 994838
```



















# Dfic vs Dmel - flam-like1

