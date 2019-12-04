
'''
A script to automate mapping reads to a reference genome
design by.https://github.com/SausanCantik

Workflow
0. Given the reads and reference in SDF format.
1. Obtain the folder name per sample
2. Create output folder per mapping
3. Define the sam format per sample
4. Use os.system(command) to execute rtg map
'''

#libarary
import os
import pandas as pd
import numpy as np

#Function to create the folder name, R1, R2 of reads

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
    print ('You now have an output file called: Sample_data.xlsx') 
    return sdf_reads_directory, R1, R2

#obtaining the parameter
sdf_reads_directory, R1, R2 = parsing_sample('reads_list_trial2.txt')

#Mapping reads to reference genome
for sample in sdf_reads_directory :
    sdf = 'Format/SDF_{}'.format(sample)
    output = 'Map/Map_{}'.format(sample)
    mapping = 'rtg map --bed-regions Ca01/Reference/ST5024G_5_targets.bed --template reference_ver01_SDF --input {} --output {} --sam-rg Read_Groups/{}.txt'.format(sdf, output, sample)
    os.system(mapping)
