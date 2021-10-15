#Plot monthly average engine rpm

#Import modules
import matplotlib.pyplot as plt
import pandas as pd

#Load dataset
df = pd.read_csv('./MachineLearning/User2_Dataset.csv', index_col = [1], parse_dates = ['Date'])
print(df.head())

#Plot monthly average engine rpm
plt.figure(figsize = (10, 8))
plt.plot(df.resample('MS').mean()['Engine RPM (rpm)'], marker = '.')
plt.ylabel('Average Engine RPM (rpm)')
plt.title('Average Engine RPM (rpm)', fontsize = 20)
plt.show()

#Plot monthly Maximum RPM
plt.figure(figsize = (10, 8))
plt.plot(df.resample('MS').max()['Engine RPM (rpm)'], marker = '.')
plt.ylabel('Maximum Engine RPM (rpm)')
plt.title('Maximum Engine RPM (rpm)', fontsize = 20)
plt.show()

#Plot monthly Minimum RPM
plt.figure(figsize = (10, 8))
plt.plot(df.resample('MS').min()['Engine RPM (rpm)'], marker = '.')
plt.ylabel('Minimum Engine RPM (rpm)')
plt.title('Minimum Engine RPM (rpm)', fontsize = 20)
plt.show()
