#Streamlit Web App
#To display Machine Learning data prediction result

#Import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sb
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

#Create title for Streamlit App
intro_page = st.title("Insurance Premium Prediction Web App")

definition = st.markdown("""
### This project aims to predict the insurance premium of a driver using Linear Regression Model
""")

#Open dataset
df = pd.read_csv('./Insurance_Dataset.csv')
#print(df.head())

#Show dataset
if st.checkbox("Show Dataset"):
        st.write(df)

#Split dataset
x = df['Distance_travelled(km)'].values.reshape(-1, 1)
y = df['Insurance_Fee'].values.reshape(-1, 1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33, random_state = 1000)
#print('Shape of x_train: ', x_train.shape, '\nShape of x_test: ', x_test.shape)
#print('Shape of y_train: ', y_train.shape, '\nShape of y_test: ', y_test.shape)

# #Select ML algorithm
model = LinearRegression()
model.fit(x_train, y_train)

#Feature scaling
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#Get Intercept and Coefficient
#st.text("Intercept Value: %.2f" % model.intercept_)
#print('Intercept Value: ', model.intercept_)
#st.text("Coefficient Value: %.2f" % model.coef_)
#print('Coefficient Value:\n', model.coef_)

#Make prediction
y_pred = model.predict(x_test)
#print('Predicted Result:\n', y_pred)

#Show Result of the data predicted
st.header("Comparison Graph between Actual Value and Predicted Value")
predicted_data = pd.DataFrame(
        {
                'Actual': y_test.flatten(), 
                'Predicted': y_pred.flatten()
        })

fig = px.bar(predicted_data, y = ["Actual", "Predicted"], labels = \
        {
                'index' : 'Driving Trip Number',
                'value' : 'Insurance Premium'
        })
st.plotly_chart(fig)

#Evaluate model
st.subheader("Model Evaluation")
mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
r2 = metrics.r2_score(y_test, y_pred)

st.text("Mean Absolute Error of The Model: %.2f" % mae)
st.text("Mean Squared Error of The Model: %.2f" % mse)
st.text("Root Mean Squared Error of The Model: %.2f" % rmse)
st.text("R2 / Accuracy Score of the Model: %.2f" % r2)

# print('Mean Absolute Error (MAE) Value: %.2f' % mae)
# print('Mean Squared Error (MSE) Value: %.2f ' % mse)
# print('Root Mean Squared Error (RMSE) Value: %.2f' % rmse)
# print('R2 Score: %.2f' % r2)