#Import modules

#Modify existing data
import pandas as pd
import numpy as np

df = pd.read_csv('./NewData/Car-Care_Dataset.csv')
#Drop time column
df.drop(['time',  'Average speed (km/h)', 'Insurance Fee'], axis = 1, inplace = True)

#Drop row with N-value
val_drop = df[df['Distance travelled (km)'] < 2].index
print(val_drop)
df.drop(val_drop, inplace = True)

#Add date column
df['Date'] = pd.date_range(start = '10/01/2020', periods = len(df), freq = 'D')
print(df['Date'])

#Rearrange column position
col_list = df[['Date', 'Distance travelled (km)', 'Engine RPM (rpm)',
            'Fuel used (L)', 'Vehicle speed (km/h)', 'Driver Type']]
df = col_list

#Rename column
col_name = {
    'Date' : 'Date',
    'Distance travelled (km)' : 'Distance_travelled(km)',
    'Engine RPM (rpm)' : 'Average_EngineRPM(rpm)',
    'Fuel used (L)' : 'Fuel_used(L)',
    'Vehicle speed (km/h)': 'Average_Vehiclespeed(km/h)',
    'Driver Type': 'Driver_Risk'
}
df = df.rename(columns = col_name)

#Change datatype
datatype = {
    'Date' : np.datetime64,
    'Distance_travelled(km)' : np.float64,
    'Average_EngineRPM(rpm)' : int,
    'Fuel_used(L)' : np.float64,
    'Average_Vehiclespeed(km/h)': int,
    'Driver_Risk': int
}
print(df.dtypes)


#Drop rows after 09/30/2021
row_del = df[df['Date'] > '2021/09/30'].index
print(row_del)
df.drop(row_del, inplace = True)

#Export to csv file
df.to_csv('./DrivingBehavior_Dataset.csv', index = True)