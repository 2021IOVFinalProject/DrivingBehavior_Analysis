#Create a New Output to CSV
#To Classify Driver

import pandas as pd
import numpy as np

df = pd.read_csv('./Preprocessing/NewData/ProcessedDataset.csv')

#Categorize Driver Based on the Type
#1 is Safe
#2 is Moderate
#3 is Dangerous
conditions = [
    (df['Vehicle speed (km/h)'] >= 0) & (df['Vehicle speed (km/h)'] <= 60),
    (df['Vehicle speed (km/h)'] > 60) & (df['Vehicle speed (km/h)'] <= 80),
    (df['Vehicle speed (km/h)'] > 80)
    ]
values = [1, 2, 3]

df['Driver Type'] = np.select(conditions, values)

#Drop time column
df.drop('time', axis = 1, inplace = True)

#Add date column
df['Date'] = pd.date_range(start = '10/01/2020', periods = len(df), freq = 'D')

#Rearrange column position
col_list = df[['Date', 'Average speed (km/h)', 'Distance travelled (km)', 'Engine RPM (rpm)',
            'Fuel used (L)', 'Vehicle speed (km/h)', 'Driver Type']]
df = col_list

#Drop rows after 09/30/2021
row_del = df[df['Date'] > '2021/09/30'].index
print(row_del)
df.drop(row_del, inplace = True)

#Export to csv file
df.to_csv('D:/Final Project/Dataset/FinalProject_Dataset.csv', index = True)