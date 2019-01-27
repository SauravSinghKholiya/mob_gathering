import numpy as np
import pandas as pd
from math import cos, asin, sqrt
import matplotlib.pyplot as plt

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
for i in range(0,arr1.shape[0],2):
    y1.append(arr1[i][0])
    x1.append(arr1[i][1])

x2 = []
y2 = []
for i in range(0,arr2.shape[0],2):
    y2.append(arr2[i][0])
    x2.append(arr2[i][1])

x3 = []
y3 = []
for i in range(0,arr3.shape[0],2):
    y3.append(arr3[i][0])
    x3.append(arr3[i][1])

st_lat = []
st_lon = []
for i in range(0,arr1.shape[0]):
    if arr1[i][2] == 0:
            st_lat.append(arr1[i][0])
            st_lon.append(arr1[i][1])

for i in range(0,arr2.shape[0]):
    if arr2[i][2] == 0:
            st_lat.append(arr2[i][0])
            st_lon.append(arr2[i][1])

for i in range(0,arr3.shape[0]):
    if arr3[i][2] == 0:
            st_lat.append(arr3[i][0])
            st_lon.append(arr3[i][1])

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.scatter(st_lon,st_lat,color="r")
plt.xlabel("latitude")
plt.ylabel("longitude")
plt.show()
