#!/bin/bash
pwd
for file in *.bed;
    do
      	if [[ $file != $1.bed ]]; then
            
            species=`echo $file | cut -d'.' -f1`
            species_ref=$1
            echo $species
            echo $species_ref
            python -m jcvi.compara.catalog ortholog $species_ref $species --no_strip_names
            python -m jcvi.graphics.dotplot $species_ref.$species.anchors
            python -m jcvi.compara.synteny depth --histogram $species_ref.$species.anchors
            python -m jcvi.compara.synteny screen --minspan=30 --simple $species_ref.$species.anchors $species_ref.$species.anchors.new
            python ../Tools/create_seqids_subset_chrom.py --species $species --directory ../$5/ --ref_species $species_ref --gtf_directory /mnt/scratchb/ghlab/sus/REFERENCE/drosophila/species/
            #python ../Tools/add_color_karyotype.py --species $species --directory ../$5/ --ref_species $species_ref --ref_directory ../$5/
            python ../Tools/add_color_karyotype_blocks.py --species $species --directory ../$5/ --ref_species $species_ref --ref_directory ../$5/  
            python -m jcvi.compara.synteny mcscan $species_ref.bed $species_ref.$species.anchors --iter=1 -o $species_ref.$species.i1.blocks
            echo $species_ref'_'$species.bed
            cat $species_ref.bed $species.bed > $species_ref'_'$species.bed
            rm blocks.layout
            python ../Tools/block_preparation.py --species_ref $species_ref --species $species --flamlike_start $3 --flamlike_end $4 --chromosome_ref $2 --n_genes 20
            python -m jcvi.graphics.synteny blocks $species_ref'_'$species.bed blocks.layout --glyphcolor=orthogroup --glyphstyle=arrow
        
        
            #rm $species_ref'_'$species.bed
            #rm $species_ref.$species.i1.blocks
            #rm blocks
            mv blocks.pdf $species_ref.$species.blocks.pdf
            mkdir plots
            mv *.pdf plots/

            
        fi
    done


