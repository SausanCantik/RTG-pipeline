
'''
A script to automate trimming fastq reads
design by.https://github.com/SausanCantik

Workflow
0. Given the reads in RAW folder. The pairends reads are consist of two bz2 files.
1. List the file names and store as a variable.
2. Use os.system(command) to execute rtg fastqtrim
'''

#libarary
import os
import pandas as pd
import numpy as np

#Function to create the folder name, R1, R2 of reads

def parsing_fastq (file): #file should be .txt
    reads = []
    i = 0
    for line in open(file):
        read = line.split()[-1]
        reads.append(read)
        i = i+1
        
    #create a file containing the sample data
    df = pd.DataFrame(reads, columns = ['fastq sample'])
    result = df.to_excel('Sample_data.xlsx')
    print ('You now have an output file called: Sample_data.xlsx') 
    return reads

#obtaining the parameter
reads = parsing_fastq('list.txt')

#trim the reads
for read in reads:
    #R = 'C:\\Users\\Biotech\\Documents\\Sausan\\NGS\\RAW\\{}'.format(read)
    R = 'F:\\Master Program\\Third Year\\INF70424-Internship\\RTG\\RAW\\{}'.format(read)
    fastqtrim = 'rtg fastqtrim -E 20 -S 20 -i {} -o Trimmed\\trimmed_{}'.format(R, read)
    os.system(fastqtrim)
