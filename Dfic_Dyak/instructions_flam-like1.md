# Dfic vs Dyak - flam-like1

### Step 1 Create a folder to run analysis with name 'Dfic_Dyak'  and add Dyak_GCF_016746365 in the file_species.txt
```
cd MCScan_plot
mkdir Dfic_Dyak
```
### Step 1: Prepare .bed and .cds files
```
cd MCScan_plot/Tools
python prepare_files.py --ref_species Dyak_GCF_016746365 --directory folder_with_saved_gtf_species_files/
```

```
cp ../Species/Dfic_GCF_018152265/Dfic_GCF_018152265.bed .
cp ../Species/Dfic_GCF_018152265/Dfic_GCF_018152265.cds .
cp ../Ref_Species/Dyak_GCF_016746365/Dyak_GCF_016746365.bed .
cp ../Ref_Species/Dyak_GCF_016746365/Dyak_GCF_016746365.cds .
cp ../Tools/run_block_comparison.sh .
```
Run the following command and define the reference species, and the location of the flamlike cluster (chromosome, start and end), e.g.:
```
bash run_block_comparison.sh Dfic_GCF_018152265 chr x y Dfic_Dyak

