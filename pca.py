from sklearn.decomposition import PCA
import pandas as pd 
from sklearn.feature_selection import VarianceThreshold
import numpy as np

df = pd.read_csv("Final_Education_Normalization.csv",encoding = 'utf-8')
cols = df.columns.values
rows = df.index.values
# print len(cols)-1
# for col in cols[1:]:
# 	vec = df[col].values
# 	value = 0
# 	count = 0
# 	for i in vec:
# 		value+=i
# 		if i!=0:
# 			count+=1
# 	if count!=0:
# 		value=value/count
# 	for i in xrange(len(rows)):
# 		if df.loc[i,col]==0:
# 			df.loc[i,col]=value
# df.to_csv("Final_Education_Normalization.csv",encoding = 'utf-8',index=False)

cols1 = cols[1:]
X=df[cols1]
# print X.columns.values
model = VarianceThreshold()
model = model.fit(X)
var = model.variances_

lis = np.argsort(var)[-10:][::-1]
print lis
lis = [cols1[i] for i in lis]
print lis
lis.insert(0,cols[0])
# print lis



df_new = df[lis]
cols = df_new.columns.values
rows = df_new.index.values
n = len(rows)
for col in cols[1:]:
	vec = df_new[col].values
df_new.to_csv("final.csv",encoding = 'utf-8',index=False)
