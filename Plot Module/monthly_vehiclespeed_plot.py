#Plot Monthly maximum speed

#Import modules
import matplotlib.pyplot as plt
import pandas as pd

#Load dataset
df = pd.read_csv('./MachineLearning/User2_Dataset.csv', index_col = [1], parse_dates = ['Date'])
print(df.head())

#Plot monthly maximum speed
plt.figure(figsize = (10, 8))
plt.plot(df.resample('MS').max()['Vehicle speed (km/h)'], marker = '.')
plt.ylabel('Maximum Vehicle Speed (km/h)')
plt.title('Maximum Vehicle Speed (km/h)', fontsize = 20)
plt.show()

#Plot monthly minimum speed
plt.figure(figsize = (10, 8))
plt.plot(df.resample('MS').min()['Vehicle speed (km/h)'], marker = '.')
plt.ylabel('Minimum Vehicle speed (km/h)')
plt.title('Minimum Vehicle Speed (km/h)', fontsize = 20)
plt.show()

#Plot monthly average
plt.figure(figsize = (10, 8))
plt.plot(df.resample('MS').mean()['Vehicle speed (km/h)'], marker = '.')
plt.ylabel('Average Vehicle Speed (km/h)')
plt.title('Average Vehicle Speed (km/h)', fontsize = 20)
plt.show()