# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:07:33 2019

@author: Mukesh
"""

import numpy as np
import matplotlib.pyplot as plt

x = [10,21,3,14,15,16]
y = np.array(x)

## Int32 is an immutable value type that represents signed integers ##
type(y)
y[0:5]
y.shape
y>10
y[y>10]


y**2
y+1
y[y%2!=0]

x = [1,2,3,4,5,6]
y = [7,8,9,10,11,12]

#np.array(y).shape


z = np.array([x,y])
z = z.reshape(4,3)

z[0,1]
z.shape

z[:,1:]

# Statistics on numpy array 
np.mean(z)
np.median(z)
np.mean(z[1,:])
np.mean(z[:,1])
np.std(z)
np.var(z)




# Few functions in numpy 
np.round(1.21212,2)

temp1 = np.random.normal(10,2,5)

temp2 = np.random.normal(-10,2,5)
help(np.random.normal)
temp2
temp1
temp3 = np.column_stack((temp1,temp2))
temp3
m1 = np.random.random((2,3))
m2 = np.random.random((2,3))

m1+m2
