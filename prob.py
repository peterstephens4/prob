#  Peter Stephens
# 5/20/2016

import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt
import collections

# Calculate the number frequencies of the data in the list "testlist"
testlist = [1, 4, 5, 6, 9, 9, 9]
c = collections.Counter(testlist)
count_sum = sum(c.values())
for k,v in c.items():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))

#  Create a boxplot and histogram for the given data in list "x"
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.figure()
plt.boxplot(x)
plt.savefig("box_plot.png")

plt.figure()
plt.hist(x, histtype='bar')
plt.savefig("histogram_plot.png")

#  Create a QQ-plot of the normal distribution
plt.figure()
test_data = np.random.normal(size=1000)   
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.savefig("normal_dist_plot.png") 

#  Create a QQ-plot of the uniform distribution
plt.figure()
test_data2 = np.random.uniform(size=1000)   
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.savefig("uniform_dist_plot.png") 