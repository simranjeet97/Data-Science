from numpy.matlib import randn
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

#Line Graph
x = np.arange(-3,3,0.001)
plt.plot(x, norm.pdf(x))
plt.show()

#Multiple Plots on One Graph
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
#Save Graph to a file
plt.savefig('D:\\Myplot.png', format='png')
plt.show()

#Adjust Axes, Add Grid, Change line type and colors
#Labeling Axes and Add Legend
axes = plt.axes()
axes.set_xlim(-5,5)
axes.set_ylim(0,1.0)
axes.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
axes.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
axes.grid()
plt.xlabel("Greebles")
plt.ylabel("Probability")
plt.plot(x, norm.pdf(x), 'b-') #Solid Blue
plt.plot(x, norm.pdf(x,1,0.5), 'g:') #Doted Green
plt.legend(['Sneetches', 'Gecks'], loc=4)
plt.show()

#PieChart
plt.rcdefaults()
values = [12,44,4,42,14]
colors = ['r','g','b','c','m']
explode = [0,0,0.2,0,0]
labels = ['India', 'USA', 'Russia', 'China', 'Europe']
plt.pie(values, colors=colors, labels=labels, explode=explode)
plt.title("Students Locations")
plt.show()

#Scatter
X = np.random.normal(10,100,100)
Y = np.random.normal(0,10,100)
plt.scatter(X, Y)
plt.show()

#Box and Whisker Plot for Quantliers
uniformskew = np.random.rand(100)*100-40
high_outlier = np.random.rand(10)* 50 + 100
low_outlier = np.random.rand(10)* -50 -100
data = np.concatenate((uniformskew, high_outlier, low_outlier))
plt.boxplot(data)
plt.show()


