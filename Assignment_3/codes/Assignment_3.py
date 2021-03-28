#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
from numpy import trapz
#our pdf is already there in library,so we just import it here
from scipy.stats import expon
import matplotlib.pyplot as plt

#here we create evenly spaced numbers in the interval [0,100]
x = np.linspace(0,100,1010)
#here we create evenly spaced numbers in the interval [1,100]
y = np.linspace(1,100,1010)
#graph settings
f1 = plt.figure()
f2 = plt.figure()
ax1 = f1.add_subplot(111)
#plotting pdf
ax1.plot(x, expon.pdf(x), 'k-', lw=2, label='pdf',color='green')
ax2 = f2.add_subplot(111)
#plotting cdf
ax2.plot(x, expon.cdf(x), 'k-', lw=2, label='cdf',color='blue')
plt.show()
#here we find area under the graph of pdf in interval y using trapezium method
#we do this because the area under pdf from 1 to infinity gives the probability of X>1.
area1=trapz(expon.pdf(y),dx=0.1)
#as calculated theoritically we find probability
area2=1-expon.cdf(1)
print('simulation=',area1,',','real=',area2)


# In[ ]:





# In[ ]:





# In[ ]:




