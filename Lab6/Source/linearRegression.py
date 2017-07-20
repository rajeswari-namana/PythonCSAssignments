#Importing modules
from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

#dummy data set
lr = linear_model.LinearRegression()
boston = datasets.load_boston()
x = boston.target

#generating y array from x data set values
y= cross_val_predict(lr, boston.data, x, cv=10)

#calculating mean of x and y values
xMean=np.mean(x)
yMean=np.mean(y)

#calculating y-intercept
B1=(np.sum((x-xMean)*(y-yMean)))/(np.sum(np.power((x-xMean),2)))

#calculating slope
B0=yMean-(B1*xMean)

#plotting graph
plt.scatter(x,y)
ry=B1*x+B0
plt.plot(x,ry,'r',lw=3)
plt.title("Housing Prices")
plt.xlabel("Cost per square foot in 100 dollars")
plt.ylabel("Square foot")
plt.show()