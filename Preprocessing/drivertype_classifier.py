#Create a New Output to CSV
#To Classify Driver

import pandas as pd
import numpy as np

df = pd.read_csv('./Driving_Behavior_Dataset.csv')

#Categorize Driver Based on the Type
#1 is Safe
#2 is Moderate
#3 is Dangerous
conditions = [
    (df['Maximum_Vehicle_Speed_(km/h)'] <= 50),
    (df['Maximum_Vehicle_Speed_(km/h)'] > 50) & (df['Maximum_Vehicle_Speed_(km/h)'] <= 100),
    (df['Maximum_Vehicle_Speed_(km/h)'] > 100)]
values = [1, 2, 3]

df['Driver_Risk'] = np.select(conditions, values)

#Export to csv file
df.to_csv('D:/Preprocessing/DrivingBehavior_Final_Dataset.csv', index = True)