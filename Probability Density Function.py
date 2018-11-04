from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import binom
from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

#uniform distribution
data = np.random.uniform(-10,10,100000)
print(data)
plt.hist(data,50, rwidth=0.5)
plt.show()

#Normal/Gaussian
#using arange function
x = np.arange(-3,3,0.001)
print(x)
#pdf function with normal distribution
plt.plot(x, norm.pdf(x))
plt.show()
#using normal function
values = np.random.normal(5.0,2.0,10000)
plt.hist(values,50)
plt.show()

#Exponential PDF / Power Law
x = np.arange(0,10,0.001)
plt.plot(x,expon.pdf(x))
plt.show()

#Bionomial Probability Mass Function (Descrete Values)
n = 10
p = 0.5
x = np.arange(0,10,0.001)
plt.plot(x, binom.pmf(x,n,p))
plt.show()

#Poission PMF
mu = 500
x = np.arange(400,600,0.5)
plt.plot(x, poisson.pmf(x, mu))
#Example- Website get average clicks 500 per day. What is odd of getting 550?
plt.show()

