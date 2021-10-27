#Driver type classifier using Naive Bayes Classifier

#Import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

#Open dataset
df = pd.read_csv('./MachineLearning/User2_Dataset.csv', index_col = [0])
#See first 5 rows of dataset
print(df.head(), '\n')
#Check datatypes of variables
print(df.dtypes, '\n')

#Count the value of the output variable to be predicted
print(df['Driver Type'].value_counts(), '\n')

#Select independent and dependent variable(s)
x = df.drop(['Date', 'Driver Type'], axis = 1)
y = df['Driver Type']

#Split dataset to train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 10)
print('Shape of x_train: ', x_train.shape, '\nShape of x_test: ', x_test.shape)
print('Shape of y_train: ', y_train.shape, '\nShape of y_test: ', y_test.shape)

#Select ML algorithm
classifier = GaussianNB()
classifier.fit(x_train, y_train)

#Predict result and probability
y_pred = classifier.predict(x_test)

#Confusion Matrix
conf_mat = metrics.confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix of the Model:\n", conf_mat)

#Show Confusion Matrix Heatmap
conf_df = pd.DataFrame(conf_mat, index = [1, 2, 3], columns = [1, 2, 3])
plt.title("Confusion Matrix's Heatmap")
sb.heatmap(conf_df, annot = True, fmt ='d', cmap = 'YlGnBu')
plt.xlabel("Predicted Classification Values")
plt.ylabel("Actual Classification Values")
plt.show()

#Classification Report
cr = metrics.classification_report(y_test, y_pred)
print("\nClassification Report of the Model:\n", cr)

#Accuracy score
score = metrics.accuracy_score(y_test, y_pred)
print('Accuracy of Naive Bayes Classifier: %.2f' % score)