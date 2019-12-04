
'''
A script to automate variant calling
design by.https://github.com/SausanCantik

Workflow
0. Given the bam files
1. Locate the template (reference)
2. Create output folder per sample
3. Define the bam file per iteration
'''

#libarary
import os
import pandas as pd
import numpy as np
from timeit import default_timer as timer

#time the execution
start = timer()

def parsing_sample (file): #file should be .txt
    sdf_reads_directory = []
    R1 = []
    R2 = []
    i = 0
    for line in open(file):
        reads = line.split()[-1]
        if i % 2 == 1:
            R2.append(reads)
        else :
            R1.append(reads)
            folder = reads.split('_')[0]
            sdf_reads_directory.append(folder)
        i = i+1
        
    #create a file containing the sample data
    df = pd.DataFrame(zip(sdf_reads_directory,R1,R2), columns = ['Folder', 'R1', 'R2'])
    result = df.to_excel('Sample_data.xlsx')
    print ('You now have an output file called: {}'.format(result)) 
    return sdf_reads_directory, R1, R2

#obtaining the parameter
sdf_reads_directory, R1, R2 = parsing_sample('reads_list_trial.txt')

#Mapping reads to reference genome
for sample in sdf_reads_directory :
    bam = 'Map/Map_{}'.format(sample)
    output = 'SNP/SNP_{}'.format(sample) 
    vcf = 'rtg snp --bed-regions targets.bed --template reference_ver01_SDF --output {} {}/alignments.bam'.format(output, bam)
    os.system(vcf)
    
end = timer()
print('running time : ', end-start)
