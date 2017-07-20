#import modules
import numpy as np
import matplotlib.pyplot as plt
import random

#take input from user for how many shirts
points=int(input("Enter number of points: "))

#taking number of clusters as 3 to group shirts into small, medium and large
clusters=3

#generating array of random weights between 100 pounds and 220 pounds
# and random weights between 50 inches and 75 inches
arr=np.array([(random.uniform(100,220),random.uniform(50,75))for i in range(points)])
weights=arr[:, 0]
heights=arr[:,1]

#Plotting points
plt.scatter(weights,heights)
plt.title("T-shirts grouping based on height & weight")
plt.xlabel("Weight (pounds)")
plt.ylabel("Height (inches)")
plt.show()

#calculating distances
def cluster_content(arr, pt):
    cluster = {}
    for x in arr:
        value = min([(i[0],np.linalg.norm(x - pt[i[0]]))for i in enumerate(pt)], key=lambda s:s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster

#calculating centers
def new_center(pt, cluster):
    keys =sorted(cluster.keys())
    newpt = np.array([(np.mean(cluster[k],axis = 0))for k in keys])
    return newpt

def matched(newpt, oldpt):
    return (set([tuple(a)for a in newpt]) == set([tuple(a)for a in oldpt]))

#plotting the clusters with colors
def plot_cluster(pt,cluster, itr):
    color = 10 * ['r.','g.','y.']
    print('Iteration number : ',itr)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=15)
    plt.scatter(pt[:,0],pt[:,1],marker = 'x', s = 150, linewidths = 10, zorder = 10)
    plt.title("T-shirts grouping based on height & weight")
    plt.xlabel("Weight (pounds)")
    plt.ylabel("Height (inches)")
    plt.show()

#kmeans clustering logic
def kmeansCluster(arr, clusters, points):
    temp1 = np.random.randint(points, size = clusters)
    oldpt = np.array([arr[i]for i in temp1])
    temp2 = np.random.randint(points, size=clusters)
    newpt = np.array([arr[i] for i in temp2])
    cluster = cluster_content(arr, oldpt)
    itr = 0
    plot_cluster(oldpt,cluster,itr)
    while not matched(newpt, oldpt):
        itr = itr + 1
        oldpt = newpt
        cluster = cluster_content(arr,newpt)
        plot_cluster(newpt, cluster,itr)
        newpt = new_center(newpt, cluster)
    plot_cluster(newpt, cluster, itr)
    return

#calling function
kmeansCluster(arr, clusters, points)
