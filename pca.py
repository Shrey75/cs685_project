from sklearn.decomposition import PCA
import pandas as pd 
from sklearn.feature_selection import VarianceThreshold
import numpy as np

df = pd.read_csv("Final_Education_Normalization.csv",encoding = 'utf-8')
cols = df.columns.values
rows = df.index.values
print len(cols)-1
X=df[cols[1:]]
# pca = PCA(n_components=10)
# pca = pca.fit(df[cols[1:]])
# print(pca.components_)

model = VarianceThreshold()
model = model.fit(X)
var = model.variances_

lis = np.argsort(var)[-10:][::-1]
lis = [cols[i] for i in lis]
lis.insert(0,cols[0])


# df_new = pd.DataFrame(columns=cols)
# for i,cunt in enumerate(countries_in_edu):
# 	if cunt not in miss_cunt:
# 		df_new.loc[i] = df.iloc[row2index[cunt]].values
# 	else:
# 		vec = np.zeros(len(df.iloc[0].values[1:]))
# 		count = 0
# 		for jj in regions[cunt2region[cunt]]:
# 			if jj not in miss_cunt:
# 				vec +=[ float(k) for k in df.iloc[row2index[jj]].values[1:]]
# 				count +=1
# 		if count!=0:
# 			vec=vec/count
# 		vec = [cunt] + [str(gg) for gg in vec]
# 		df_new.loc[i] = vec
# print len(df_new[cols[0]].values)
# df_new = df_new.sort_values(by=cols[0])
# df_new = df_new.reset_index(drop=True)
# df_new.to_csv("newdata/education3/"+file,encoding = 'utf-8',index=False)

df_new = df[lis]
cols = df_new.columns.values
rows = df_new.index.values
n = len(rows)
for col in cols[1:]:
	vec = df_new[col].values
	value = 0
	count = 0
	for i in vec:
		value+=i
		if i!=0:
			count+=1
	if count!=0:
		value=value/count
	for i in xrange(n):
		if df_new.loc[i,col]==0:
			df_new.loc[i,col]=value
df_new.to_csv("final.csv",encoding = 'utf-8',index=False)