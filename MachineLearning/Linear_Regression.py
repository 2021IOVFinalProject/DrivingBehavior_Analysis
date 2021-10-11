#Linear Regression to predict outcome of Fuel used and Distance travelled

#Import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Open dataset
df = pd.read_csv('./MachineLearning/User2_Dataset.csv', index_col = [0])
print(df.columns)

#Show heatmap of feature correlation
dfcorr = df.corr()
sb.heatmap(dfcorr, cmap = 'YlGnBu', annot = True)
plt.title("Features Correlation Heatmap")
plt.tight_layout()
plt.show()

#Create ML Model
#Split dataset
x = df['Fuel used (L)'].values.reshape(-1, 1)
y = df['Distance travelled (km)'].values.reshape(-1, 1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33, random_state = 100)

#Plot scatter of data before model predicts
plt.scatter(x_test, y_test, color = 'navy')
plt.title('Scatter Plot of Fuel Used in Certain Distance')
plt.xlabel('Fuel Used (L)')
plt.ylabel('Distance Travelled (km)')
plt.show()

#Select ML algorithm
model = LinearRegression()
model.fit(x_train, y_train)

#Get Intercept and Coefficient
#print('Intercept Value: ', model.intercept_)
#print('Coefficient Value:\n', model.coef_)

#Make prediction
y_pred = model.predict(x_test)
#print('Predicted Result:\n', y_pred)

#Compare actual value with predicted value
data = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
#print(data)

# Visualize the comparison results.
df1 = data.head(30)
df1.plot(kind='bar', figsize=(10, 8), color = ['darkblue', 'limegreen'])
plt.title('Projected Predicted Driving Distance and Comparison with Original Value')
plt.xlabel('Driving Trip Number')
plt.ylabel('Driving Distance (km)')
plt.show()

#Evaluate model
mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
r2 = metrics.r2_score(y_test, y_pred)
print('Mean Absolute Error (MAE) Value: %.2f' % mae)
print('Mean Squared Error (MSE) Value: %.2f ' % mse)
print('Root Mean Squared Error (RMSE) Value: %.2f' % rmse)
print('R2 Score: %.2f' % r2)

'''
#Standardize the dataset
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
'''