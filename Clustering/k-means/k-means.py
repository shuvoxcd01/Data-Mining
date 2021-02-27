# -*- coding: utf-8 -*-]
"""
Created on Sun Nov 19 16:29:06 2017

@author: Falguni Das Shuvo
"""

import pandas as pd
import matplotlib.pyplot as plt
import random
from math import sqrt, pow

def euclidian_distance(point1, point2):
    return sqrt(pow((point1[0] - point2[0]),2) +  pow((point1[1] - point2[1]), 2))

def listOfTuples_to_listOfLists(l):    
    x=[]
    y=[]
    
    for each_tuple in l:
        x.append(each_tuple[0])
        y.append(each_tuple[1])
        
    return [x,y]

l2l = listOfTuples_to_listOfLists

def getCentroid(list_of_tuples):
    l = l2l(list_of_tuples)
    x = l[0]
    y = l[1]
    
    sum_x = sum(x)
    sum_y = sum(y)
    
    len_x = float(len(x))
    len_y = float(len(y))
    
    centroid = (sum_x/len_x, sum_y/len_y)
    
    return centroid

df = pd.read_excel("Book1.xlsx","Sheet1")
total_tuples = df.shape[0]

points = []

for i in range(0,total_tuples):
    points.append(tuple(df.iloc[i].tolist()))


k = 5
c = random.sample(range(0,total_tuples),k)
centroid_list = []
for each_c in c:
    centroid_list.append(tuple(df.iloc[each_c].tolist()))


f = open("k_means_calculations.txt", 'w')
f.write("k = " + str(k) + '\n')


_iter = 0;

while True:
    clusters = []
    for each_k in range(0,k):
        clusters.append([])
        
    for point in points:
        distance = []
        for i in range(0,k):
            distance.append(euclidian_distance(centroid_list[i], point))
        
        clusters[distance.index(min(distance))].append(point)
        
    f.write("Iteration: " + str(_iter) +  "\n")
    f.write("Centroid list:  " + str(centroid_list) + "\n")  
    for i in range(0,k):
        f.write("Cluster with centroid " + str(centroid_list[i]) + ":    ")
        f.write(str(clusters[i]) + '\n')
    
        
    plt_axis_limit = df['x'].max()+1
    if df['y'].max() > plt_axis_limit:
        plt_axis_limit = df['y'].max()+1
    
    plt.axis([0,plt_axis_limit, 0, plt_axis_limit])
    
    for cluster in clusters[:]:
        p = l2l(cluster)
        plt.plot(p[0],p[1], 'o')
    #plt.show()
    #plt.close() 
    
    _c = l2l(centroid_list)
    plt.plot(_c[0],_c[1], '+')
    
    plt.title("Figure__k="+str(k)+"__iteration="+str(_iter))
    plt.savefig("Figure__k="+str(k)+"__iteration="+str(_iter))
    plt.show()
    plt.close()
    
    old_centroid_list = centroid_list[:]
   # print centroid_list
    
    for i in range(0,k):
        centroid_list[i] = getCentroid(clusters[i])  #new centroid list
    
    #print centroid_list
    if old_centroid_list == centroid_list:
        break
    
    _iter = _iter + 1
        


f.close()





    