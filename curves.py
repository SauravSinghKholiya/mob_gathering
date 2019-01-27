import numpy as np
import pandas as pd
from math import cos, asin, sqrt
import matplotlib.pyplot as plt
from math import cos, asin, sqrt,atan,degrees
import statistics

saurav = pd.read_csv("Sauravgps.csv")
saurav = saurav.loc[:, ['lat','lon','speed']]
shail = pd.read_csv("shailengps.csv")
shail = shail.loc[:, ['lat','lon','speed']]
vinay =pd.read_csv("vinaygps.csv")
vinay = vinay.loc[:, ['lat','lon','speed']]

arr1 = saurav.values
arr2 = shail.values
arr3 = vinay.values

x1 = []
y1 = []
turn_points_x1 = []
turn_points_y1 = []
for i in range(0,arr1.shape[0]):
    y1.append(arr1[i][0])
    x1.append(arr1[i][1])

x2 = []
y2 = []
turn_points_x2 = []
turn_points_y2 = []
for i in range(0,arr2.shape[0]):
    y2.append(arr2[i][0])
    x2.append(arr2[i][1])

x3 = []
y3 = []
turn_points_x3 = []
turn_points_y3 = []
for i in range(0,arr3.shape[0]):
    y3.append(arr3[i][0])
    x3.append(arr3[i][1])

m1 = (y1[1] - y1[0])/(x1[1] - x1[0])
for i in range(1,arr1.shape[0]-1,2):
    if(x1[i+1] != x1[i]):
        m2 = (y1[i+1] - y1[i])/(x1[i+1] - x1[i])
        angle = degrees(atan((m1-m2)/(1+m1*m2)))
        if abs(angle) >= 5:
            turn_points_x1.append(x1[i])
            turn_points_x1.append(x1[i+1])
            turn_points_y1.append(y1[i])
            turn_points_y1.append(y1[i+1])
        m1 = m2

m1 = (y2[1] - y2[0])/(x2[1] - x2[0])
for i in range(1,arr2.shape[0]-1,2):
    if(x2[i+1] != x2[i]):
        m2 = (y2[i+1] - y2[i])/(x2[i+1] - x2[i])
        angle = degrees(atan((m1-m2)/(1+m1*m2)))
        if abs(angle) >= 5:
            turn_points_x2.append(x2[i])
            turn_points_x2.append(x2[i+1])
            turn_points_y2.append(y2[i])
            turn_points_y2.append(y2[i+1])
        m1 = m2

m1 = (y3[1] - y3[0])/(x3[1] - x3[0])
for i in range(1,arr3.shape[0]-1,2):
    if(x3[i+1] != x3[i]):
        m2 = (y3[i+1] - y3[i])/(x3[i+1] - x3[i])
        angle = degrees(atan((m1-m2)/(1+m1*m2)))
        if abs(angle) >= 5:
            turn_points_x3.append(x3[i])
            turn_points_x3.append(x3[i+1])
            turn_points_y3.append(y3[i])
            turn_points_y3.append(y3[i+1])
        m1 = m2

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.scatter(turn_points_x1,turn_points_y1,color="r")
plt.scatter(turn_points_x2,turn_points_y2,color="y")
plt.scatter(turn_points_x3,turn_points_y3,color="b")
plt.xlabel("latitude")
plt.ylabel("longitude")
plt.show()
