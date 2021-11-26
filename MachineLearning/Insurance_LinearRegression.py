import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Open dataset
df = pd.read_csv('./MachineLearning/Insurance_Dataset.csv')

print(df.head())
print(df.columns)

#Split dataset to label and target
x = df['Distance_travelled(km)'].values.reshape(-1, 1)
y = df['Insurance_Fee'].values.reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
print('Shape of x_train: ', x_train.shape, '\nShape of x_test: ', x_test.shape)
print('Shape of y_train: ', y_train.shape, '\nShape of y_test: ', y_test.shape)

#Feature scaling
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#Select Machine Learning Model
model = LinearRegression()
model.fit(x_train, y_train)

#Retrieve Intercept and Coefficient
print('Intercept Value: ', model.intercept_)
print('Coefficient Value:\n', model.coef_)

#Make prediction
y_pred = model.predict(x_test)
#print('Predicted Result:\n', y_pred)

#Compare actual value with predicted value
result = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(result)

# Visualize the comparison results.
df1 = result.head(30)
df1.plot(kind='bar', figsize=(10, 8))
plt.title('Actual vs Predicted')
plt.xlabel('Driving Trip Number')
plt.ylabel('Insurance Premium')
plt.grid(which='major', linewidth='0.5', color= 'black')
plt.grid(which='minor', linewidth='0.5', color= 'green')
plt.show()

#Evaluate model
mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
r2 = metrics.r2_score(y_test, y_pred)
print('Mean Absolute Error (MAE) Value: ', mae)
print('Mean Squared Error (MSE) Value: ', mse)
print('Root Mean Squared Error (RMSE) Value: ', rmse)
print('R2 Score: ', r2)