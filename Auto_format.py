
'''
A script to automate formating fastq reads files to rtg's SDF
design by.https://github.com/SausanCantik

Workflow
0. Given the reads in RAW folder. The pairends reads are consist of two bz2 files.
1. List the file names and store as a variable.
2. Parse the R1 (identify from behind) and store as a variable
3. Parse the R2 (identify from behind) and store as a variable
4. Use os.system(command) to execute rtg format
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
sdf_reads_directory, R1, R2 = parsing_sample('list2.txt')

#convert pair ends fastq tp SDF
for i in range(len(R1)) :
    output = 'Format-trimmed\\SDF_{}'.format(sdf_reads_directory[i])
    left = 'C:\\Users\\Biotech\\Documents\\Sausan\\RTG\\rtg-core-non-commercial-3.10.1-windows-x64\\rtg-core-non-commercial-3.10.1\\Trimmed\\{}'.format(R1[i])
    right = 'C:\\Users\\Biotech\\Documents\\Sausan\\RTG\\rtg-core-non-commercial-3.10.1-windows-x64\\rtg-core-non-commercial-3.10.1\\Trimmed\\{}'.format(R2[i])
    fastq_to_sdf = 'rtg format -f fastq -q sanger -o {} -l {} -r {}'.format(output, left, right)
    os.system(fastq_to_sdf)
    
