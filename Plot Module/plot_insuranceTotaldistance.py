#Import modules
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./MachineLearning/User2_Dataset.csv', index_col = [1], parse_dates = ['Date'])
print(df.columns)

dist_resample = df.resample('M').sum()['Distance travelled (km)']
print(dist_resample)

ax = dist_resample.plot.bar(color = 'darkblue')
ax.set_xticklabels(dist_resample.index.strftime('%Y-%m-%d'))
plt.xlabel('Month')
plt.ylabel('Total Distance (km)')
plt.title('Total Distance Driven per Month')
plt.tight_layout()
plt.show()