#import modules
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

#random x and y values
x=[1,2,3,4,5,6,74,17,4,25,36,7,89,10]
y=[22,23,24,25,26,65,78,79,76,54,34,67,8,77]

#plot the points
plt.scatter(x,y)
plt.title("Finding plant species based on leaf length & width")
plt.ylabel("Leaf width (mms)")
plt.xlabel("Leaf length (mms)")
plt.show()

# Concatenate arrays & generate the linkage matrix
arr=np.concatenate((x,y),)
Z = linkage(arr, 'ward')

#plot the dendrogram or the hierarchical diagram
dendrogram(Z)
plt.title("Finding plant species based on leaf length & width")
plt.ylabel("Leaf width (mms)")
plt.xlabel("Leaf length (mms)")
plt.show()