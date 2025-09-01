# nf-core_McCleary_RNAseq

Reference: https://nf-co.re/configs/mccleary/

Step 1: 
Make a spreadsheet which has header:
```
sample,fastq_1,fastq_2,strandedness
```

Step 2: 
```
python3 make_samplesheet.py -i path/to/folder/where/RNAseq_data/is/available
```

or if the file of each run is in a folder and you want to make one file at the end
```
python3 make_samplesheet1.py -i /gpfs/gibbs/pi/kwan/TAA_feb12/ycga-gpfs/sequencers/illumina/sequencerX/runs/20240205_LH00309_0137_B223TWKLT4/Data/Intensities/BaseCalls/Unaligned/Project_Maz9/Sample_* -o samplesheet1.csv
```

Step 3:
Use local_config.sh
and run the bash script
```
sbatch nfcore_bash.sh
```
