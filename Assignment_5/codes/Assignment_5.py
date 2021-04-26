#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
import array as arr

sample_size = 5000
event_size = 0
prob_theo = 0.6
urn = ['r']*40+['b']*60
data = ['a']*5000
#we use the fact that numbering the balls doesn't change the probability of drawing a ball, because here number is independent of colour
#So, numbering the balls or not, the probability remains same
for i in range(sample_size):
    #here we draw an array in a random order of r's and b's without replacement
    draw = np.random.choice(urn, replace = 'False', size = 100)
    data[i] = draw[99] 
    #Now, we check whether the last ball drawn is black and increase event_size
    if(draw[99] =='b'):
        event_size+=1
print('Therefore, the probability of theory vs simulation is:',prob_theo,event_size/sample_size)

plt.hist(data, bins = 3)
plt.ylabel('Frequency(Out of 5000 simulations)')
plt.xlabel('colour of last ball drawn')
plt.show()


# In[ ]:




