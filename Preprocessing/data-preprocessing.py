#Python program to process raw dataset

#Import modules
import numpy as np
import os
import pandas as pd

#Locate dataset
os.chdir('./Data/')
fileloc = os.listdir()

#Create lists to store important features and data
total_distance = list()
avg_rpm = list()
max_rpm = list()
avg_speed = list()
max_speed = list()

#Open dataset
for csv_file in fileloc:
    df = pd.read_csv(csv_file)
    #print(csv_file, '\n', df.columns)

#Remove unused columns
    df.drop(df.columns[df.columns.str.contains('Unnamed')], axis = 1, inplace = True)
    df.drop(df[['Average speed (km/h)', 'Average fuel consumption (L/100km)',
            'Average fuel consumption (total) (L/100km)', 'Barometric pressure (kPa)',
            'Calculated boost (bar)', 'Fuel economizer (based on fuel system status and throttle position) ()',
            'Distance travelled (total) (km)', 'Calculated instant fuel consumption (L/100km)',
            'Calculated instant fuel rate (L/h)', 'Fuel used price ($)', 'Fuel used (total) (L)', 
            'Fuel used (L)', 'Fuel used price (total) ($)', 'Intake air temperature (℃)',
            'Intake manifold absolute pressure (kPa)', 'Instant engine power (based on fuel consumption) (hp)',
            'Throttle position (%)', 'Vehicle acceleration (g)']], axis = 1, inplace = True)
    print(csv_file, '\n', df.columns)

#Extract features from dataset
#Get maximum values of columns
    mx_spd = df['Vehicle speed (km/h)'].max()
    mx_rpm = df['Engine RPM (rpm)'].max()
    dist = df['Distance travelled (km)'].max()
#Get avg values of columns
    avg_spd = df['Vehicle speed (km/h)'].mean()
    avg_engine_rpm = df['Engine RPM (rpm)'].mean()
#Append to list
    total_distance.append(dist)

    avg_rpm.append(avg_engine_rpm)
    avg_speed.append(avg_spd)
    
    max_rpm.append(mx_rpm)
    max_speed.append(mx_spd)


#Create new dataframe
new_file = {
    'Driving_Distance_(km)' : total_distance,
    'Avg_Engine_RPM_(rpm)' : avg_rpm,
    'Avg_Vehicle_Speed_(km/h)': avg_speed,
    'Maximum_Engine_RPM_(rpm)': max_rpm,
    'Maximum_Vehicle_Speed_(km/h)': max_speed
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
    'Date' : np.datetime64,
    'Maximum_Vehicle_Speed_(km/h)' : int,
    'Maximum_Engine_RPM_(rpm)' : int,
    'Avg_Vehicle_Speed_(km/h)' : int,
    'Avg_Engine_RPM_(rpm)' : int,
    'Driving_Distance_(km)' : float
}
new_df = new_df.astype(datatype)
print(new_df.dtypes)

#Export to new csv file
new_df.to_csv('./Allen_Collected_Dataset.csv', index = True)

'''
#Drop rows after 09/30/2021
row_del = df[df['Date'] > '2021/09/30'].index
print(row_del)
df.drop(row_del, inplace = True)
'''