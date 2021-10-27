#Streamlit Web App
#To display Machine Learning data prediction result

#Import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sb
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

#Create title for Streamlit App
intro_page = st.title("Car-Care Driving Behavior Analysis Machine Learning Prediction Web App")

definition = st.markdown("""
## Problem Statement
This project aims to predict and analyze the driving behavior of drivers by using 
Machine Learning Model (Linear Regression and Naive Bayes Classifier).
    
#### Some important problems to be analyzed and predicted:
- Does every features has a strong relationship or correlation?
- How accurate is the model?
- Is there any data visualization function available?
- What is going to be predicted?
    -   Our goal is to create an interactive web-app where user can select their preferred
        features to be used in X and Y in order to predict the future outcome value using the
        Linear Regression Model.
    
    -   While the Naive Bayes Classifier is a classification model where the model will predict
        the target feature and will display the output of the result without allowing users to
        select their own features to predict the outcome.
	
##### Features In Dataset
- Average speed (km/h)
- Distance travelled (km)
- Engine RPM (rpm)
- Fuel used (L)
- Vehicle speed (km/h)
- Driver Type
""")

#Open dataset
df = pd.read_csv('./User2_Dataset.csv',index_col = [0])
#print(df.head())
df.drop('Date', axis = 1, inplace = True)

select_menu = st.header("Please Click the Menu on the left for More Functions")

st.sidebar.title("Main Menu")
st.sidebar.subheader("Select Your Options")
menu_select = st.sidebar.selectbox(label = "Features", options = ['Exploratory Data Analysis', 'Machine Learning'])

#EDA
if menu_select == 'Exploratory Data Analysis':
    if st.sidebar.checkbox("Show Dataset"):
        st.subheader('Driving Behavior Dataset')
        st.write(df)

#Show heatmap of feature correlation
    dfcorr = df.corr()
    if st.sidebar.checkbox("Show Features Correlation Heatmap"):
        fig, ax = plt.subplots()
        st.title("Features Correlation Heatmap")
        sb.heatmap(dfcorr, cmap = 'YlGnBu', annot = True, ax = ax)
        st.write(fig)

#Show histogram of every features in dataset
    if st.sidebar.checkbox("Show Histogram"):
        select_box = st.selectbox(label = "Features / Columns", options = df.columns)
        sb.distplot(df[select_box])
        st.pyplot()

#Show scatter plot of features
    if st.sidebar.checkbox("Show Scatter Plot"):
        col1 = st.selectbox("Which feature(s) for X?", df.columns[:6])
        col2 = st.selectbox("Which feature(s) for Y?", df.columns[:7])
        fig = px.scatter(df, x = col1, y = col2)
        st.plotly_chart(fig)

#Machine Learning
if menu_select == 'Machine Learning':
    st.sidebar.subheader('Machine Learning Data Prediction')
#Create sidebar for Machine Learning model selection
    algorithms_list = ['Linear Regression', 'Naive Bayes Classifier']
    model = st.sidebar.selectbox("Select Machine Learning Model", algorithms_list)

#Create selectbox for Machine Learning menu
    if model == 'Linear Regression':
        ml_model = LinearRegression()
        col1 = st.selectbox("Which feature(s) for X?", df.columns[0:5])
        col2 = st.selectbox("Which feature(s) for Y?", df.columns[0:6])
        #Show Scatter Plot correlation between X and Y
        st.subheader('Scatter Plot Correlation Between X and Y Chosen')
        fig = px.scatter(df, x = col1, y = col2)
        st.plotly_chart(fig)

# #Split dataset
        x = df[col1].values.reshape(-1, 1)
        y = df[col2].values.reshape(-1, 1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33, random_state = 100)

# #Select ML algorithm
        regression_model = LinearRegression()
        regression_model.fit(x_train, y_train)

#Get Intercept and Coefficient
        #print('Intercept Value: ', model.intercept_)
        #print('Coefficient Value:\n', model.coef_)

#Make prediction
        y_pred = regression_model.predict(x_test)
        #print('Predicted Result:\n', y_pred)

#Show Result of the data predicted
        st.header("Comparison Graph between Actual Value and Predicted Value")
        predicted_data = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
        df1 = predicted_data['Actual'].head(30)
        st.subheader("Actual Value")
        act_fig = px.bar(df1, y = 'Actual',  labels= \
                {'Actual':'Fuel Consumed (L) per Trip',\
                'index': 'Driving Trip'}).update_traces(marker = dict(color = 'green'))
        st.plotly_chart(act_fig)

        df2 = predicted_data['Predicted'].head(30)
        st.subheader("Predicted Value")
        act_fig = px.bar(df2, y = 'Predicted', labels= \
                {'Predicted':'Predicted Fuel Consumed (L) per Trip',\
                'index': 'Driving Trip'}).update_traces(marker = dict(color = 'red'))
        st.plotly_chart(act_fig)
        #df1.plot(kind='bar', figsize=(10, 8), color = ['darkblue', 'limegreen'])
        #plt.title('Projected Predicted Driving Distance and Comparison with Original Value')
        #plt.xlabel('Driving Trip Number')
        #plt.ylabel('Driving Distance (km)')
        #plt.show()

#Evaluate model
        st.subheader("Model Evaluation")
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
        r2 = metrics.r2_score(y_test, y_pred)
        # print('Mean Absolute Error (MAE) Value: %.2f' % mae)
        # print('Mean Squared Error (MSE) Value: %.2f ' % mse)
        # print('Root Mean Squared Error (RMSE) Value: %.2f' % rmse)
        # print('R2 Score: %.2f' % r2)
        st.text("Mean Absolute Error of The Model: %.2f" % mae)
        st.text("Mean Squared Error of The Model: %.2f" % mse)
        st.text("Root Mean Squared Error of The Model: %.2f" % rmse)
        st.text("R2 / Accuracy Score of the Model: %.2f" % r2)


#Naive Bayes Classifier
    if model == 'Naive Bayes Classifier':
#Select independent and dependent variable(s)
        x = df.drop(['Driver Type'], axis = 1)
        y = df['Driver Type']

#Split dataset to train and test
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 10)
        #print('Shape of x_train: ', x_train.shape, '\nShape of x_test: ', x_test.shape)
        #print('Shape of y_train: ', y_train.shape, '\nShape of y_test: ', y_test.shape)

#Train Machine Learning algorithm
        classifier = GaussianNB()
        classifier.fit(x_train, y_train)
    
#Predict result
        y_pred = classifier.predict(x_test)

#Confusion Matrix
        conf_mat = metrics.confusion_matrix(y_test, y_pred)
        conf_df = pd.DataFrame(conf_mat, index = [1, 2, 3], columns = [1, 2, 3])
        #print("\nConfusion Matrix of the Model:\n", conf_mat)
        st.subheader("Confusion Matrix of the Classifier")
        st.write(conf_df)

#Classification Report
        cr = metrics.classification_report(y_test, y_pred)
        #print("\nClassification Report of the Model:\n", cr)
        st.subheader("Classification Report of the Model")
        st.text(cr)

#Calculate the accuracy of model
        score = metrics.accuracy_score(y_test, y_pred)
        #print('Accuracy of Classifier: %.2f' % score)
        st.text("Accuracy of Classifier: %.2f" % score)