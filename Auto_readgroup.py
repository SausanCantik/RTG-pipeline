import os

# a function to create folder name, R1, R2 of the reads

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
    #df = pd.DataFrame(zip(sdf_reads_directory,R1,R2), columns = ['Folder', 'R1', 'R2'])
    #result = df.to_excel('Sample_data.xlsx')
    #print ('You now have an output file called: Sample_data.xlsx') 
    return sdf_reads_directory, R1, R2
#==========================================================================
# a function to create read_group.txt automatically based on the plate name

def create_rg (file):
    sdf_reads_directory, R1, R2 = parsing_sample(file)
    for sample in sdf_reads_directory :
        RG = '@RG\tID:NB501358\tSM:{}\tPL:ILLUMINA'.format(sample)
        command = 'echo {} > {}.txt'.format(RG, sample)
        os.system(command)
#==========================================================================
path = 'C:/Users/Biotech/Documents/Sausan/RTG/rtg-core-non-commercial-3.10.1-windows-x64/rtg-core-non-commercial-3.10.1/reads_list_trial2.txt'
create_rg(path)
