import os 

path = os.chdir("/Users/nihalnihalani/Desktop/dataset/covid")

i = 0

for file in os.listdir(path):
    
    new_file_name = "Covid_patient_{}.jpg".format(i)
    
    os.rename(file, new_file_name)
    
    i = i+1
