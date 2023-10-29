#!/bin/bash
#SBATCH --mem 512
#SBATCH --job-name gene_syn
#SBATCH --time=0-00:60:00


conda activate gene_synteny
python 2create_maps.py --species $1 --directory_read $2 --directory_write $3


