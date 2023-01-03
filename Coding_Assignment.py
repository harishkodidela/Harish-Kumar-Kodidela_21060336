'''Plotting work as per the set of observations linking the amount of rain per year and field
productivity in a dry area somewhere in Central America.'''

#Import the required packages for plotting the graphs to visualize data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

#Read the data from excel or any other format of data by using pandas.
os.chdir(r"C:\Users\Admin\Desktop\Data Science\Fundamentals")
list_items = os.listdir()
data = pd.read_csv(r"inputdata6.csv", sep=',')

#Plot the scatter by using above data as Rainfall vs Productivity
image_dir = 'Images'
x = np.array(data['Rainfall'])
x = x.reshape((-1,1))
y = np.array(data['Productivity'])
plt.Figure(figsize=(16,8),dpi=1000)

#Use labels, linestyles, marker and color for better visualization
plt.scatter(x, y, linestyle = "solid", marker = "*", color = "red")

#Use title, xlabel, ylabel and legend for good understanding of graph
plt.title("Amount of rain per year v/s productivity in dry areas")
plt.xlabel("Amount of Precipitation")
plt.ylabel("Productivity Coefficient")
plt.show()

'''Use of Linear Regression computes the estimators of coefficient and directly the predicted weights.
The association between the data points is used in linear regression to create a straight line connecting all 
of them and predicting the future value which is done in code.'''
design = LinearRegression()
design.fit(x,y)
score = design.score(x,y)
intercept = design.intercept_
coef = design.coef_
yfit = intercept + coef*x

#Predicting the productivity coefficiesnt for value X given in assignment
rainfall = 245
predicted_productivity_coefficient = design.predict([[rainfall]])
print(predicted_productivity_coefficient)

plt.figure(figsize=(16,10),dpi=1000)
plt.plot(x,yfit, label = 'Model Regression')
##Use labels, linestyles, marker and color for better visualization
plt.scatter(x, y, linestyle = "solid", marker = "*", color = "red", label = "Actual Observations")
plt.scatter(rainfall, predicted_productivity_coefficient, label = "Predicted Value: 0.11426791", color = "green", linewidths=(5))
#Use title, xlabel, ylabel and legend for good understanding of graph
plt.title("Amount of rain per year v/s productivity in dry areas")
plt.xlabel("Amount of Precipitation")
plt.ylabel("Productivity Coefficient")
#Using the legend and locating the position
plt.legend(loc = "lower right", prop={'size': 18})
plt.show()

'''The above plots describes a set of observations linking the amount of
rain per year and field productivity in a dry areas and based on the linear 
regression model, the productivity coefficient of the field if the amount
of precipitations is X mm (given in the assignment task) was calculated.'''


