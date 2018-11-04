import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

incomes = np.random.normal(100,20,500)
print(incomes)
print(stats.mode(incomes))
plt.hist(incomes, 50 , color='Black', alpha=0.3, rwidth=.85)
#hist, edge = np.histogram(incomes)
#print(hist)
#print(edge)
print(incomes.std())
print(incomes.var())

plt.show()
