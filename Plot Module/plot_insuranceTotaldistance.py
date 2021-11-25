#Import modules
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./MachineLearning/DrivingBehavior_Dataset.csv', index_col = [1], parse_dates = ['Date'])
print(df.columns)

#Resample dataset
dist_resample = df.resample('15D').sum()['Distance_travelled(km)']
print(dist_resample)

ax = dist_resample.plot.bar(color = 'darkblue')
ax.set_xticklabels(dist_resample.index.strftime('%Y-%m-%d'))
plt.xlabel('Month')
plt.ylabel('Total Distance (km)')
plt.title('Total Distance Driven per Month')
plt.tight_layout()
plt.show()

#Convert dist_resample to dataframe
new_df = pd.DataFrame(data = dist_resample)
print(new_df.head())

#Export to new dataset
new_df.to_csv('./MachineLearning/Insurance_DrivingDistance_Dataset.csv', index = True)