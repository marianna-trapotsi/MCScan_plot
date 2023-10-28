#!/bin/bash
#SBATCH --mem 512
#SBATCH --job-name gene_syn
#SBATCH --time=0-00:60:00


#module load miniconda3-4.7.12.1-gcc-9.2.0-cg3qrnj
#source activate gene_synteny

cd ../Species/$1/ 
cp ../../Ref_Species/$2/$2.bed .
cp ../../Ref_Species/$2/$2.cds .

python -m jcvi.compara.catalog ortholog $2 $1 --no_strip_names
python -m jcvi.graphics.dotplot $2.$1.anchors
python -m jcvi.compara.synteny depth --histogram $2.$1.anchors

mkdir -p plots

python ../../Tools/create_seqids.py --species $1 --ref_species $2 --ref_directory ../../Ref_Species/$2/ --directory ../../Species/$1/
python -m jcvi.compara.synteny screen --minspan=30 --simple $2.$1.anchors $2.$1.anchors.new
python ../../Tools/create_seqids_subset_chrom.py --species $1 --directory ../../Species/$1/ --ref_species $2 --gtf_directory folder_with_saved_gtf_species_files/

rm layout
sed -e 's/species1/'$2'/g' -e 's/species2/'$1'/g' ../../Tools/layout_ref>> layout

python -m jcvi.graphics.karyotype seqids layout
mv karyotype.pdf $2_$1_karyotype.pdf


python ../../Tools/add_color_karyotype.py --species $1 --directory ../Species/$1/ --ref_species $2 --ref_directory ../../Ref_Species/
python -m jcvi.graphics.karyotype seqids layout

mv karyotype.pdf $2_$1_color_karyotype.pdf
mv *.pdf plots

rm $2.bed
rm $2.cds
