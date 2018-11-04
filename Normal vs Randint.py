import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(10,100,500)
print(data)

data_two = np.random.normal(50,100,500)
print(data_two)

plt.hist(data,50, rwidth=0.5)
plt.show()
plt.hist(data_two,50, rwidth=0.5)
plt.show()

#See Difference in both the graphs, normal graph is slightly inline at top but randint graph is like a mountain.