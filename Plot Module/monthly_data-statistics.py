##Plot monthly data statistics

#Import modules
import matplotlib.pyplot as plt
import pandas as pd

#Load dataset
df = pd.read_csv('./MachineLearning/DrivingBehavior_Final_Dataset.csv', index_col = [1], parse_dates = ['Date'])
print(df.head())

#Plot monthly average engine rpm
plt.figure(figsize = (10, 8))
plt.plot(df.resample('MS').mean()['Avg_Engine_RPM_(rpm)'], marker = '.')
plt.ylabel('Average Engine RPM (rpm)')
plt.title('Average Engine RPM (rpm)', fontsize = 20)

#Plot monthly Maximum RPM
plt.figure(figsize = (10, 8))
plt.plot(df.resample('MS').max()['Maximum_Engine_RPM_(rpm)'], marker = '.')
plt.ylabel('Maximum Engine RPM (rpm)')
plt.title('Maximum Engine RPM (rpm)', fontsize = 20)

#Plot monthly average vehicle speed
plt.figure(figsize = (10, 8))
plt.plot(df.resample('MS').mean()['Avg_Vehicle_Speed_(km/h)'], marker = '.')
plt.ylabel('Average Vehicle Speed (km/h)')
plt.title('Average Vehicle Speed (km/h)', fontsize = 20)

#Plot monthly maximum vehicle speed
plt.figure(figsize = (10, 8))
plt.plot(df.resample('MS').max()['Maximum_Vehicle_Speed_(km/h)'], marker = '.')
plt.ylabel('Maximum Vehicle Speed (km/h)')
plt.title('Maximum Vehicle Speed (km/h)', fontsize = 20)
plt.show()