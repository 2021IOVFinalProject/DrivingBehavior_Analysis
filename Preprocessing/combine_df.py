#Python program to concatenate all datasets

#Import modules
import os
import pandas as pd

os.chdir('D:/Final Project/Preprocessing/NewData/')
file_loc = os.listdir()

csv_list = list()
for csv_file in file_loc:    
    df = pd.read_csv(csv_file, header = 0, index_col = [0])
    csv_list.append(df)

new_df = pd.concat(csv_list, axis = 0, ignore_index = False)

new_df.to_csv('D:/Final Project/Preprocessing/NewData/ProcessedDataset.csv', index = True)
print("Processing Done\nThank You")