#Driver Dangerous Level Machine Learning Classification Model Prediction Module

#Import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

#Open dataset
df = pd.read_csv('./MachineLearning/DrivingBehavior_Final_Dataset.csv', index_col = [0])
#See first 5 rows of dataset
print(df.head(), '\n')
#Check datatypes of variables
print(df.dtypes, '\n')
#Check statistics of dataset
print(df.describe())

#Count the value of the output variable to be predicted
print(df['Driver_Risk'].value_counts(), '\n')

#Select independent and dependent variable(s)
x = df.drop(['Date', 'Driver_Risk'], axis = 1)
y = df['Driver_Risk']

#Split dataset to train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 20)
print('Shape of x_train: ', x_train.shape, '\nShape of x_test: ', x_test.shape)
print('Shape of y_train: ', y_train.shape, '\nShape of y_test: ', y_test.shape)

#Feature Scaling
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#Select ML algorithm
classifier = GaussianNB()
classifier.fit(x_train, y_train)

#Predict result
y_pred = classifier.predict(x_test)

#Confusion Matrix
conf_mat = metrics.confusion_matrix(y_test, y_pred)
conf_df = pd.DataFrame(conf_mat, index = [1, 2, 3], columns = [1, 2, 3])
print("\nConfusion Matrix of the Model:\n", conf_mat)
plt.title("Confusion Matrix's Heatmap")
sb.heatmap(conf_df, annot = True, fmt ='d', cmap = 'YlGnBu')
plt.xlabel("Actual Classification Values")
plt.ylabel("Predicted Classification Values")
plt.show()

#Classification Report
cr = metrics.classification_report(y_test, y_pred)
print("\nClassification Report of the Model:\n", cr)

#Accuracy score
score = metrics.accuracy_score(y_test, y_pred)
print('Accuracy of Naive Bayes Classifier: %.2f' % score)