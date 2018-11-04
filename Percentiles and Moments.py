import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

#Percentiles
vals = np.random.normal(300,100,1000)
plt.hist(vals, 100, rwidth=0.5)
print(np.percentile(vals, 50)) #also called median percentile
print(np.percentile(vals, 90)) #that means all the values are less then this values at 90
print(np.percentile(vals, 20))
plt.show()

#Moments - Mean, Variance, Skew, Kurtosis
data = np.random.normal(0,10,10000)
#FIRST MOMENT
print(np.mean(data))
print(np.var(data))
print(sp.skew(data))
print(sp.kurtosis(data))
plt.hist(data,50)
plt.show()


