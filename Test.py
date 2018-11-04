from numpy.matlib import randn
from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

uniformskew = np.random.rand(100)*100-40
high_outlier = np.random.rand(10)* 50 + 100
low_outlier = np.random.rand(10)* -50 -100
data = np.concatenate((uniformskew, high_outlier, low_outlier))
plt.boxplot(data)
plt.show()
