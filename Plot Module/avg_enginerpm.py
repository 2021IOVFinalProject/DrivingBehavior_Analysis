#Plot monthly average engine rpm

#Import modules
import matplotlib.pyplot as plt
import pandas as pd

#Load dataset
df = pd.read_csv('./MachineLearning/FinalProject_Dataset.csv', index_col = [1], parse_dates = ['Date'])
print(df.head())

#Plot monthly average engine rpm
plt.figure(figsize = (10, 8))
plt.plot(df.resample('MS').mean()['Engine RPM (rpm)'], marker = '.')
plt.ylabel('Average Engine RPM (rpm)')
plt.title('Average Engine RPM (rpm)', fontsize = 20)
plt.show()