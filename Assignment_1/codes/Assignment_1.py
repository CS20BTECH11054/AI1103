import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns

sample_size=10000
event_size=9920
event_size_reqd=80
#prob for X=1, i.e., probability for 2 students not having same birthday
prob=event_size/sample_size
#prob for X=0, i.e, probability for 2 students having same birthday
prob_reqd=event_size_reqd/sample_size
#creating random variables
data_bern = bernoulli.rvs(size=sample_size,p=prob)
#checking for X=0
err_ind = np.nonzero(data_bern == 0)
#finding the size of err_ind,i.e., number of cases where X=1 and dividing it by sample size 
err_n = np.size(err_ind)/sample_size

#Theory vs Simulation
print(prob,err_n)
# settings for seaborn plot 
ax= sns.distplot(data_bern,kde=False,color="green",hist_kws={'alpha':1})
plt.ylim(0, 1000)
ax.set(xlabel='Bernoulli', ylabel='Frequency')
plt.savefig('../../figures/probexm/probexm1.eps')
plt.show()