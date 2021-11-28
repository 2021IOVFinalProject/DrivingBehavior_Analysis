#Module for Exploratory Data Analysis

#Import modules
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

#Open dataset
df = pd.read_csv('./MachineLearning/DrivingBehavior_Dataset.csv', index_col = [0])
df.drop(['Date', 'Driver_Risk'], axis = 1, inplace = True)
#print(df.columns)

#Print top rows of dataset
print(df.head())

#Print shape of dataset
print(df.shape)

#Descriptive statistics
print(df.describe())

#Skew of Data
print(df.skew())

#Show histogram bar of all features in dataset to show the number of population
df.hist()
plt.show()

#Density plot to get a quick idea of the distribution of each attribute
df.plot(kind = 'density', subplots = True, layout = (3,3), sharex = False)
plt.show()

#Print correlation between columns in dataset
# print(df.corr(method = 'pearson'))

#Show heatmap of feature correlation
dfcorr = df.corr()
sb.heatmap(dfcorr, cmap = 'YlGnBu', annot = True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()