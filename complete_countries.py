# -*- coding: utf-8 -*-
import pandas as pd 
import os
import pickle as pkl
import numpy as np
import csv
files = os.listdir("newdata/education")


countries = []
regions = {}
regions['Pacific'] = []
country_name2region ={}
countries_in_edu = []
for file in files:
	if file == '.DS_Store':
		continue
	df = pd.read_csv("newdata/education2/"+file,encoding = 'utf-8')
	cols = df.columns.values
	rows = list(set(df[cols[0]].values))
	countries_in_edu = countries_in_edu +rows
countries_in_edu = (list(set(countries_in_edu)))
# for i in (countries_in_edu):
# 	# if i[0]!='B':
# 	print i



regions['Europe'] = []
df1 =  pd.read_csv("./UNSD-Methodology.csv", encoding = 'utf-8')
cols =  df1.columns.values
for j,i in enumerate(df1[cols[3]].values):
	if i == 'Eswatini':
		i = 'Swaziland'
	if i == 'United States of America':
		i = 'United States'
	if i == 'Cabo Verde':
		i = 'Cape Verde'
	if i == 'Czechia':
		i = 'Czech Republic'
	if i == 'United Kingdom of Great Britain and Northern Ireland':
		i = 'United Kingdom'
	if i == u"Côte d’Ivoire":
		i = "C\xc3\xb4te d'Ivoire".decode('utf-8')
	if i not in countries_in_edu:
		continue
	
	countries.append(i)
	if df1.iloc[j,1] not in regions:
		regions[df1.iloc[j,1]] = [i]
	else:
		regions[df1.iloc[j,1]].append(i)
	if df1.iloc[j,2] == df1.iloc[j,2]:
		if df1.iloc[j,2] not in regions:
			regions[df1.iloc[j,2]] = [i]
		else:
			regions[df1.iloc[j,2]].append(i)
	if df1.iloc[j,0]=='Oceania':
		regions['Pacific'].append(i)
regions ['South Asia'] =regions['Southern Asia']

del regions['Latin America and the Caribbean']
del regions['Southern Asia']
del regions['Melanesia']
del regions['Micronesia']
del regions['Sub-Saharan Africa']
del regions['Polynesia']
del regions['Australia and New Zealand']

for i in regions:
	lis = regions[i]
	for j in lis:
		country_name2region[j]=i
for file in files:
	if file == '.DS_Store':
		continue
	print file
	df = pd.read_csv("newdata/education2/"+file,encoding = 'utf-8')
	cols = df.columns.values
	print len(df[cols[0]].values)
	rows = list(set(df[cols[0]].values))
	row2index = {}
	for i,row in enumerate(df[cols[0]].values):
		row2index[row]=i
	miss_country_name = []
	for country_name in countries_in_edu:
		if country_name in rows:
			if df.iloc[row2index[country_name],1]!=df.iloc[row2index[country_name],1] or df.iloc[row2index[country_name],1] == 0:
				miss_country_name.append(country_name)
				rows.remove(country_name)
		else:
			miss_country_name.append(country_name)
	df_new = pd.DataFrame(columns=cols)
	for i,country_name in enumerate(countries_in_edu):
		if country_name not in miss_country_name:
			df_new.loc[i] = df.iloc[row2index[country_name]].values
		else:
			vec = np.zeros(len(df.iloc[0].values[1:]))
			count = 0
			for jj in regions[country_name2region[country_name]]:
				if jj not in miss_country_name:
					vec +=[ float(k) for k in df.iloc[row2index[jj]].values[1:]]
					count +=1
			if count!=0:
				vec=vec/count
			vec = [country_name] + [str(gg) for gg in vec]
			df_new.loc[i] = vec
	print len(list(set(df_new[cols[0]].values)))
	df_new = df_new.sort_values(by=cols[0])
	df_new = df_new.reset_index(drop=True)
	df_new.to_csv("newdata/education3/"+file,encoding = 'utf-8',index=False)
