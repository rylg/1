# -*- coding: utf-8 -*-
"""1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1trpt4SmlWiVzobwLV1Kcxx18vslyVq2f
"""

import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as metrics

data = [
        (10, 95),
        (9, 80),
        (2, 10),
        (15, 50),
        (10, 45),
        (16, 98),
        (11, 38),
        (16, 93),
]

x = []
for i in range(0, len(data)):
    ptx = data[i][0]
    x.append(ptx)

y = []
for i in range(0, len(data)):
    pty = data[i][1]
    y.append(pty)

xx = []
for i in range(0, len(x)):
    x2 = x[i]*x[i]
    xx.append(x2)

xy = []
for i in range(0, len(y)):
    x2 = x[i]*y[i]
    xy.append(x2)

s_x = np.sum(x)
s_y = np.sum(y)
s_xx = np.sum(xx)
s_xy = np.sum(xy)

n = len(x)

m = (n*s_xy - s_x*s_y)/(n*s_xx - s_x*s_x)
b = (s_y - m*s_x)/n

plt.scatter(x,y)
plt.show()

plt.clf()

# plt.scatter(x,y)

# x_val = range(0,17)
# y_val = m*x_val + b
# plt.plot(x_val,y_val,color="red")

# plt.show()
# plt.clf()

#Get prediction for all the datapoints
y_pred=[]

for point in data:
    xp=point[0]
    y_pred.append(m*xp+b)

# print(y_pred)

#PLot the points and regression line
plt.scatter(x,y)
plt.plot(x,y_pred,color="green")
plt.show()

d=np.array(y)-np.array(y_pred)
#print(d)
mse_f = np.mean(d**2)
mae_f = np.mean(abs(d))
rmse_f = np.sqrt(mse_f)
r2_f = 1-(sum(d**2)/sum((y-np.mean(y))**2))

print("Results by manual calculation:")
print("MAE:",mae_f)
print("MSE:", mse_f)
print("RMSE:", rmse_f)
print("R-Squared:", r2_f)
#print("Accuracy_score",acc)

mae = metrics.mean_absolute_error(y, y_pred)
mse = metrics.mean_squared_error(y, y_pred)
rmse = np.sqrt(mse) #mse**(0.5)  
r2 = metrics.r2_score(y,y_pred)

print("Results of sklearn.metrics:")
print("MAE:",mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R-Squared:", r2)