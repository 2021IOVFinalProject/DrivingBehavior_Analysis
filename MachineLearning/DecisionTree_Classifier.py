#Driver Dangerous Level Machine Learning Classification Model Prediction Module

#Import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree

#Load dataset
df = pd.read_csv('./MachineLearning/DrivingBehavior_Final_Dataset.csv', index_col = [0])

#EDA
print(df.head())
print(df.columns)
print(df.describe())
print(df.shape)

#Correlation heatmap
dfcorr = df.corr()
sb.heatmap(dfcorr, cmap = 'YlGnBu', annot = True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

#Select target variable and features
x = df.drop(['Date', 'Driver_Risk'], axis = 1)
y = df['Driver_Risk']

#Split dataset to train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33, random_state = 100)
print('Shape of x_train: ', x_train.shape, '\nShape of x_test: ', x_test.shape)
print('Shape of y_train: ', y_train.shape, '\nShape of y_test: ', y_test.shape)

#Feature Scaling
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#Model the tree
classifier = DecisionTreeClassifier()
classifier.fit(x_train, y_train)

#Predict the model
y_pred = classifier.predict(x_test)

#Classification Report
cr = metrics.classification_report(y_test, y_pred)
print("\nClassification Report of the Model:\n", cr)

#Accuracy score
score = metrics.accuracy_score(y_test, y_pred)
print('Accuracy of Decision Tree Classifier: %.2f' % score)

#Confusion Matrix
conf_mat = metrics.confusion_matrix(y_test, y_pred)
conf_df = pd.DataFrame(conf_mat, index = [1, 2, 3], columns = [1, 2, 3])
print("\nConfusion Matrix of the Model:\n", conf_mat)
plt.title("Confusion Matrix's Heatmap")
sb.heatmap(conf_df, annot = True, fmt ='d', cmap = 'YlGnBu')
plt.xlabel("Actual Classification Values")
plt.ylabel("Predicted Classification Values")
plt.show()

#Visualizing Decision Tree
tree_visualization = plot_tree(decision_tree = classifier, feature_names = df.columns,
        class_names = ["Safe", "Moderate", "Dangerous"], filled = True, precision = 4, rounded = True)
plt.show()