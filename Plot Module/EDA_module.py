#Module for Exploratory Data Analysis

#Import modules
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

#Open dataset
df = pd.read_csv('./MachineLearning/User1_Dataset.csv', index_col = [1])
df.drop(df.columns[df.columns.str.contains('Unnamed')], axis = 1, inplace = True)
df.drop('Driver Type', axis = 1, inplace = True)
print(df.columns)

#Print top rows of dataset
#print(df.head())

#Print shape of dataset
#print(df.shape)

#Descriptive statistics
#print(df.describe())

#Skew of Data
#print(df.skew())

#Show histogram bar of all features in dataset to show the number of population
df.hist()
plt.show()

#Density plot to get a quick idea of the distribution of each attribute
# df.plot(kind = 'density', subplots = True, layout = (3,3), sharex = False)
# plt.show()

#Print correlation between columns in dataset
# print(df.corr(method = 'pearson'))

#Show heatmap of feature correlation
# dfcorr = df.corr()
# sb.heatmap(dfcorr, cmap = 'YlGnBu', annot = True)
# plt.title("Correlation Heatmap")
# plt.tight_layout()
# plt.show()

#Show relation between some features using regression plot
sb.regplot(x = 'Fuel used (L)', y = 'Distance travelled (km)', data = df, color = 'navy')
plt.title('Data Distribution and Relation Between Fuel Used and Distance Travelled')
plt.show()

sb.regplot(x = 'Vehicle speed (km/h)', y = 'Engine RPM (rpm)', data = df)
plt.title('Data Distribution and Relation Between Vehicle Speed and Engine RPM')
plt.show()

sb.regplot(x = 'Average speed (km/h)', y = 'Distance travelled (km)', data = df, color = 'darkblue')
plt.title('Data Distribution and Relation Between Average Speed and Distance Travelled')
plt.show()