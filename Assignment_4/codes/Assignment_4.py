#!/usr/bin/env python
# coding: utf-8

# In[49]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math
import random

#here we create evenly spaced numbers in the interval [0,100]
x = np.linspace(0,100,1010)
#here we create evenly spaced numbers in the interval [1,100]
y = np.linspace(1,100,1010)

#We define the CDF function of the exponential distribution in terms of lambda and x
def CDFExponential(lamb,x): #lamb = lambda
    cdf=1-np.exp(-lamb*x)
    return cdf
def PDFExponential(lamb,x):
    pdf=np.exp(-lamb*x)
    return pdf
#Function to compute the value of lambda from the mean
def lamb_from_MeanExponential(mean):
    return 1/mean;
Mean = 2
lamb_da = lamb_from_MeanExponential(Mean)
#graph settings
f1 = plt.figure()
f2 = plt.figure()
ax1 = f1.add_subplot(111)
ax2 = f2.add_subplot(111)
#plotting cdf
ax1.plot(x, CDFExponential(lamb_da,x), 'k-', lw=2, label='cdf',color='green')
ax1.set(title="CDF",xlabel="x",ylabel="CDF")
#plotting pdf
ax2.plot(x, PDFExponential(lamb_da,x), 'k-', lw=2, label='pdf',color='blue')
ax2.set(title="PDF",xlabel="x",ylabel="PDF")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




