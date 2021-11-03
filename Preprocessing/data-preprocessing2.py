#This program is to extract features from datasets provided by Advisor of this project professor David Li

#Import modules
from numpy import datetime64, select
import pandas as pd

df = pd.read_csv('./DavidDrivingBehavior_synthetic_data_new_1.csv')
print(df.columns)
#print(df.describe())

#Drop User ID 2 data
id_del = df[df['UserID'] == 2].index
df.drop(id_del, inplace = True)

#Create new dataframe
new_file = {
    'Driving_Distance_(km)' : df['DrivingDistance'],
    'Avg_Vehicle_Speed_(km/h)' : df['Avg_Speed'],
    'Avg_Engine_RPM_(rpm)' : df['Avg_engine_rpm'],
    'Maximum_Engine_RPM_(rpm)': df['Max_engine_rpm'],
    'Maximum_Vehicle_Speed_(km/h)': df['Max_speed']
}

new_df = pd.DataFrame(new_file)
print(new_df.head())
print(new_df.shape)

#Add date column
new_df['Date'] = pd.date_range(start = '10/01/2020', periods = len(new_df), freq = 'D')
print(new_df['Date'])

#Rearrange column position
col_list = new_df[['Date', 'Avg_Vehicle_Speed_(km/h)', 
                'Maximum_Vehicle_Speed_(km/h)',
                'Maximum_Engine_RPM_(rpm)', 'Avg_Engine_RPM_(rpm)',
                'Driving_Distance_(km)']]
new_df = col_list
print(new_df)

#Change datatype
datatype = {
    'Date' : datetime64,
    'Maximum_Vehicle_Speed_(km/h)' : int,
    'Maximum_Engine_RPM_(rpm)' : int,
    'Avg_Vehicle_Speed_(km/h)' : int,
    'Avg_Engine_RPM_(rpm)' : int,
    'Driving_Distance_(km)' : float
}
new_df = new_df.astype(datatype)
print(new_df.dtypes)

#Drop dates after 09/30
date_del = new_df[new_df['Date'] > '2021/09/30'].index
new_df.drop(date_del, inplace = True)

#Export to csv file
new_df.to_csv('./David_Dataset_Manipulated.csv', index = False)