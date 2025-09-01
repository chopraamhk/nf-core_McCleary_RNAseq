# nf-core_McCleary_RNAseq

Reference: https://nf-co.re/configs/mccleary/

Step 1: 
Make a spreadsheet which has header:
```
sample,fastq_1,fastq_2,strandedness
```

Step 2: 
```
python3 make_samplesheet.py -i /gpfs/gibbs/pi/kwan/TAA_data/
```

Step 3:
Use local_config.sh
and run the bash script
