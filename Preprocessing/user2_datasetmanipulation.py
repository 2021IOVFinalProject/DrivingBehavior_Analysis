#Import modules

#Modify existing data
import pandas as pd
import numpy as np

df = pd.read_csv('./Preprocessing/NewData/Car-Care_Dataset.csv')
#Drop time column
df.drop(['time', 'Insurance Fee'], axis = 1, inplace = True)

#Set column datatype to int
df = df.astype(int)

val_drop = df[df['Distance travelled (km)'] < 2].index
print(val_drop)
df.drop(val_drop, inplace = True)

#Add date column
df['Date'] = pd.date_range(start = '10/01/2020', periods = len(df), freq = 'D')
print(df['Date'])

#Rearrange column position
col_list = df[['Date', 'Average speed (km/h)', 'Distance travelled (km)', 'Engine RPM (rpm)',
            'Fuel used (L)', 'Vehicle speed (km/h)', 'Driver Type']]
df = col_list

#Drop rows after 09/30/2021
row_del = df[df['Date'] > '2021/09/30'].index
print(row_del)
df.drop(row_del, inplace = True)

#Export to csv file
df.to_csv('D:/Final Project/MachineLearning/User2_Dataset.csv', index = True)