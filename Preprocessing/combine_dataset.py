#Python program to combine datasets

#Import module
import numpy as np
import pandas as pd

df1 = pd.read_csv('./Data/Allen_Collected_Dataset.csv')
df2 = pd.read_csv('./David_Dataset_Manipulated.csv')
df3 = pd.read_csv('./DavidDrivingBehavior_synthetic_data_new_1.csv')

#Drop User ID 2 data
id_del = df3[df3['UserID'] == 2].index
df3.drop(id_del, inplace = True)

#Combine two datasets
new_df = pd.concat([df1, df2], axis = 0, ignore_index = True)
new_df.drop_duplicates(subset = 'Date', keep = 'first', inplace = True)
new_df['Number_of_Accelerating'] = df3['Numbers_fast_accelerating_10']
new_df['Number_of_HardBraking'] = df3['Numbers_hard_braking_9']

#Rearrange column position
col_list = new_df[['Date', 'Avg_Vehicle_Speed_(km/h)', 
                'Maximum_Vehicle_Speed_(km/h)',
                'Maximum_Engine_RPM_(rpm)', 'Avg_Engine_RPM_(rpm)',
                'Driving_Distance_(km)', 'Number_of_Accelerating', 'Number_of_HardBraking']]
new_df = col_list

#Change datatype
datatype = {
    'Date' : np.datetime64,
    'Maximum_Vehicle_Speed_(km/h)' : int,
    'Maximum_Engine_RPM_(rpm)' : int,
    'Avg_Vehicle_Speed_(km/h)' : int,
    'Avg_Engine_RPM_(rpm)' : int,
    'Driving_Distance_(km)' : float,
    'Number_of_Accelerating' : int,
    'Number_of_HardBraking': int
}
new_df = new_df.astype(datatype)

new_df.to_csv('./Driving_Behavior_Dataset.csv', index = False)
print("Processing Done\nThank You")