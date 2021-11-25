#Python module to modify result from plot_insuranceTotalDistance.py

#Import modules
import numpy as np
import pandas as pd

#Open dataset
df = pd.read_csv('./MachineLearning/Insurance_DrivingDistance_Dataset.csv', parse_dates = ['Date'])
print(df.head())

#Modify date values
df['Date'] = df['Date'].dt.strftime('%Y-%m')
print(df.head(12))

#Count discount for Insurance
count1 = int(250* 0.4)
count2 = int(250 * 0.3)
count3 = int(250 * 0.1)

#Count total price after discount
newval1 = 250 - count1
newval2 = 250 - count2
newval3 = 250 - count3

conditions = [
    (df['Distance_travelled(km)'] >= 0) & (df['Distance_travelled(km)'] <= 100),
    (df['Distance_travelled(km)'] > 100) & (df['Distance_travelled(km)'] <= 300),
    (df['Distance_travelled(km)'] > 300)]
values = [newval1, newval2, newval3]
df['Insurance_Fee'] = np.select(conditions, values)
print(df.head(12))

#Export to new csv file
df.to_csv('./MachineLearning/Insurance_Dataset.csv', index = False)