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
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

#Create title for Streamlit App
intro_page = st.title("Car-Care Driving Behavior Analysis Machine Learning Prediction Web App")

definition = st.markdown("""
## Problem Statement
This project aims to predict and classify drivers using 
Machine Learning Classification Model (Decision Tree and Naive Bayes Classifier).
    
### Features In Dataset
- Average Vehicle Speed (km/h)
- Average Engine RPM (rpm)
- Distance travelled (km)
- Fuel Used (L)
- Driver Risk
""")

#Open dataset
df = pd.read_csv('./MachineLearning/DrivingBehavior_Dataset.csv',index_col = [0])

select_menu = st.header("Please Click the Menu on the left for More Functions")

st.sidebar.title("Main Menu")
st.sidebar.subheader("Select Your Options")
menu_select = st.sidebar.selectbox(label = "Features", options = ['Exploratory Data Analysis', 'Classification Result'])

#EDA
if menu_select == 'Exploratory Data Analysis':
    if st.sidebar.checkbox("Show Dataset"):
        st.subheader('Driving Behavior Dataset')
        st.write(df)
    df.drop('Date', axis = 1, inplace = True)
#Show correlation heatmap
    dfcorr = df.corr()
    if st.sidebar.checkbox("Show Correlation Heatmap"):
        fig, ax = plt.subplots()
        st.title("Correlation Heatmap")
        sb.heatmap(dfcorr, cmap = 'YlGnBu', annot = True, ax = ax)
        st.write(fig)

#Show histogram of features in dataset
    if st.sidebar.checkbox("Show Histogram"):
        select_box = st.selectbox(label = "Feature", options = df.columns)
        sb.distplot(df[select_box])
        st.pyplot()


#Machine Learning
if menu_select == 'Classification Result':
    st.sidebar.subheader('Machine Learning Driver Classifier Prediction')
#Create sidebar for Machine Learning model selection
    algorithms_list = ['Decision Tree', 'Naive Bayes Classifier']
    model = st.sidebar.selectbox("Select Machine Learning Classification Model", algorithms_list)
#Create selectbox for Machine Learning menu
#Naive Bayes Classifier
    if model == 'Naive Bayes Classifier':
#Select independent and dependent variable(s)
        x = df.drop(['Date', 'Driver_Risk'], axis = 1)
        y = df['Driver_Risk']

#Split dataset to train and test
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 20)
        #print('Shape of x_train: ', x_train.shape, '\nShape of x_test: ', x_test.shape)
        #print('Shape of y_train: ', y_train.shape, '\nShape of y_test: ', y_test.shape)

#Feature Scaling
        scaler = StandardScaler()
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.transform(x_test)

#Train Machine Learning algorithm
        classifier = GaussianNB()
        classifier.fit(x_train, y_train)

#Predict result
        y_pred = classifier.predict(x_test)

#Confusion Matrix
        conf_mat = metrics.confusion_matrix(y_test, y_pred)
        conf_df = pd.DataFrame(conf_mat, index = [0, 1, 2, 3], columns = [0, 1, 2, 3])
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


#Decision Tree
    if model == 'Decision Tree':
#Select target variable and features
        x = df.drop(['Date', 'Driver_Risk'], axis = 1)
        y = df['Driver_Risk']

#Split dataset to train and test
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 25)
        #print('Shape of x_train: ', x_train.shape, '\nShape of x_test: ', x_test.shape)
        #print('Shape of y_train: ', y_train.shape, '\nShape of y_test: ', y_test.shape)

#Feature Scaling
        scaler = StandardScaler()
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.transform(x_test)

#Model the tree
        classifier = DecisionTreeClassifier()
        classifier.fit(x_train, y_train)

#Predict the model
        y_pred = classifier.predict(x_test)

#Confusion Matrix
        conf_mat = metrics.confusion_matrix(y_test, y_pred)
        conf_df = pd.DataFrame(conf_mat, index = [0, 1, 2, 3], columns = [0, 1, 2, 3])
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