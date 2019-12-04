'''
A script to automate rtg calibration
design by.https://github.com/SausanCantik

Workflow
0. Given the bam files
1. Locate the template (reference)
2. Define the bam file per iteration
3. Use os.system(command) to execute rtg calibrate
'''

#libarary
import os
import pandas as pd
import numpy as np

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

#Calibrate the bam file
for sample in sdf_reads_directory :
    bam = 'Map/Map_{}'.format(sample)
    #the template is in folder [reference_ver01_SDF]
    calibrate = 'rtg calibrate --template reference_ver01_SDF {}/alignments.bam'.format(bam)
    os.system(calibrate)
