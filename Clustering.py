import os 
import sys
import pandas as pd
import csv
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 
import pickle as pkl
from sklearn.cluster import AgglomerativeClustering
path = "./merge.csv"
points = pd.read_csv(path)
country = points.iloc[:,[0]].values
cols = points.columns.values
points = points[cols[1:]]
clustering = AgglomerativeClustering(n_clusters=8).fit(points)
a= list(clustering.labels_)
dic = {0:[], 1:[], 2:[], 3:[], 4:[],5:[],6:[],7:[]}
# print d
for i in range(len(a)):
	dic[a[i]].append(country[i][0])

	

lis = []

for i in dic.keys():
	for j in dic[i]:
		lis.append([j,i])

with open("Education_Clusters.csv", 'wb')  as csv_file:
	writer = csv.writer(csv_file)
	for i in lis:
		writer.writerow(i)




	for i in range(10):
		print a.count(i+1)
