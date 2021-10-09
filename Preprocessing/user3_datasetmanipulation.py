#Dataset manipulation for user3

import numpy as np
import pandas as pd

df = pd.read_csv('./Preprocessing/User3_Dataset.csv', index_col = [0])
print(df.columns)

df.drop(['Date', 'UserID', 'Numbers_fast_accelerating_8', 'Numbers_fast_accelerating_9',
        'Numbers_fast_accelerating_10', 'Numbers_fast_accelerating_11', 'Numbers_fast_accelerating_12',
        'Numbers_fast_accelerating_13', 'Numbers_fast_accelerating_14', 'Numbers_fast_accelerating_15',
        'Numbers_fast_accelerating_16', 'Numbers_fast_accelerating_17', 'Numbers_hard_braking_8',
        'Numbers_hard_braking_9', 'Numbers_hard_braking_10', 'Numbers_hard_braking_11', 'Numbers_hard_braking_12',
        'Numbers_hard_braking_13', 'Numbers_hard_braking_14', 'Numbers_hard_braking_15', 'Numbers_hard_braking_16',
        'Numbers_hard_braking_17', 'Avg_coolant_temperature', 'Max_coolant_temperature', 'Min_coolant_temperature',
        'Avg_engine_rpm', 'Min_engine_rpm'], axis = 1, inplace = True)

#Drop value of driving distance
print(df.shape)
df = df.astype(int)
drop_val = df[df['DrivingDistance'] > 35].index
print(drop_val)
df.drop(drop_val, inplace = True)
print(df.columns)
print(df.shape)

#Rename column
df.rename({'DrivingDistance' : 'Distance travelled (km)',
            'Avg_Speed' : 'Average speed (km/h)',
            'Max_engine_rpm' : 'Average engine RPM (rpm)',
            'Max_speed': 'Vehicle speed (km/h)'}, axis = 1, inplace = True)
print(df.columns)

#Drop value of vehicle speed
drop_val = df[df['Vehicle speed (km/h)'] >= 90].index
print(drop_val)
df.drop(drop_val, inplace = True)
print(df.shape)

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

#Add date column
df['Date'] = pd.date_range(start = '10/01/2020', periods = len(df), freq = 'D')
print(df['Date'])

#Arrange column list
col_list = df[['Date', 'Average speed (km/h)', 'Distance travelled (km)', 'Average engine RPM (rpm)',
            'Vehicle speed (km/h)', 'Driver Type']]
df = col_list

#Drop rows after 09/30/2021
row_del = df[df['Date'] > '2021/09/30'].index
print(row_del)
df.drop(row_del, inplace = True)

#Export to csv file
df.to_csv('D:/Final Project/MachineLearning/User3_Dataset.csv', index = True)

print(df['Distance travelled (km)'].sum())