#!/bin/sh 
#SBATCH --time=07-00:00:00
#SBATCH --job-name="nf-core"
#SBATCH -o RNAseq.o%j
#SBATCH -e RNAseq.e%j
#SBATCH --mail-user=mehak.chopra@yale.edu
#SBATCH --cpus-per-task=2
#SBATCH --mem=5G
#SBATCH --mail-type=ALL
#SBATCH --partition=week

#curl -s https://get.sdkman.io | bash
#sdk install java 17.0.10-tem

#java -version

#curl -s https://get.nextflow.io | bash
#chmod +x nextflow
#module load nf-core
module load Java/17.0.4
export NXF_WRAPPER_STAGE_FILE_THRESHOLD='40000'

module load Nextflow/25.04.6
nextflow run nf-core/rnaseq --input samplesheet.csv --outdir results_rnaseq --genome GRCh38 -profile mccleary -c local.config
