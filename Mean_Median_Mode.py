import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

incomes = np.random.normal(27000,15000,10000)
print("Incomes are -")
print(incomes)
print(np.mean(incomes))
#plt.hist(incomes,50)
#plt.show()
print(np.median(incomes))

#now Skew with more income of some person
new=np.append(incomes, [10000000000])
print(np.median(new))
print(np.mean(new))

#Mode

ages = np.random.randint(18, high=90, size=500)
print(ages)
print(stats.mode(ages))