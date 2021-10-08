#Plot monthly distance travelled

#Import modules
import matplotlib.pyplot as plt
import pandas as pd

#Load dataset
df = pd.read_csv('./MachineLearning/User1_Dataset.csv', index_col = [1], parse_dates = ['Date'])
print(df.head())

#Plot monthly distance travelled
plt.figure(figsize = (10, 8))
plt.plot(df.resample('MS').sum()['Distance travelled (km)'], marker = '.')
plt.ylabel('Distance Travelled (km)')
plt.title('Monthly Mileage (km)', fontsize = 20)
plt.show()