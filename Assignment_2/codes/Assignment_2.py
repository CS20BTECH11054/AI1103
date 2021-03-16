import numpy as np
from scipy.stats import randint
from scipy.stats import uniform
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

#here low and high values means that the discrete random variable X can take the values in the range [low,high)
low, high = 1,7
#finding variance
mean, var, skew, kurt = randint.stats(low, high, moments='mvsk')
print(var)
#plotting number on die vs probability
sample = [1,2,3,4,5,6]
freqs = {1,1,1,1,1,1}
probs = [1/6,1/6,1/6,1/6,1/6,1/6]
x_axis = list(set(sample))
ax.set(xlabel='number on die', ylabel='probability')
plt.bar(x_axis, probs)
