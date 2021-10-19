#Plot monthly fuel consumption

#Import modules
import matplotlib.pyplot as plt
import pandas as pd

#Load dataset
df = pd.read_csv('./MachineLearning/User2_Dataset.csv', index_col = [1], parse_dates = ['Date'])
print(df.head())

#Plot fuel used monthly
plt.figure(figsize = (10, 8))
plt.plot(df.resample('MS').sum()['Fuel used (L)'], marker = '.')
plt.ylabel('Fuel Consumed (L)')
plt.title('Total Fuel Consumption per Month', fontsize = 20)
plt.show()

fuel_resample = df.resample('M').sum()['Fuel used (L)']
ax = fuel_resample.plot.bar(color = 'darkblue')
ax.set_xticklabels(fuel_resample.index.strftime('%Y-%m-%d'))
plt.xlabel('Month')
plt.ylabel('Total Fuel Consumption (L)')
plt.title('Total Fuel Consumption per Month', fontsize = 20)
plt.tight_layout()
plt.show()

#Plot average fuel consumption
plt.figure(figsize = (10, 8))
plt.plot(df.resample('MS').mean()['Fuel used (L)'], marker = '.')
plt.ylabel('Average Fuel Consumption (L)')
plt.title('Average Fuel Consumption per Month', fontsize = 20)
plt.show()