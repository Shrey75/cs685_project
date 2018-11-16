from sklearn.decomposition import PCA
import pandas as pd 
from sklearn.feature_selection import VarianceThreshold
import numpy as np
import re

df_new = pd.DataFrame()
for i, file in enumerate(["Final_Education.csv","health.csv"]):
	print file
	df = pd.read_csv(file)
	if i==0:
		df_new = df
	else:
		del df[df.columns.values[0]]
		df_new = pd.concat([df_new, df], axis=1)
		
new_path = "./merge_wn_missing.csv"

df =df_new
cols = df.columns.values
for col in cols[1:]:
	vec = df[col].values
	value = 0
	count = 0
	for i in vec:
		value+=i
		if i!=0:
			count+=1
	if count!=0:
		value=value/count
	for i in xrange(len(df[cols[0]].values)):
		if df.loc[i,col]==0:
			df.loc[i,col]=value




cols = pd.read_csv("Final_Education.csv").columns.values[1:]
# print len(cols)
for j,i in enumerate(cols):
	i = i.split('_')[0]
	cols[j] = re.sub('[0-9][0-9][0-9]+','',i)
cols = list(set(cols))
# print len(cols)
for i in cols:
	# print '\\item  ',i

# df_new.to_csv(new_path, index = False)