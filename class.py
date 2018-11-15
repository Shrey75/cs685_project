# -*- coding: utf-8 -*-
import pandas as pd 
import os
import pickle as pkl
import numpy as np
import csv
from sklearn import tree
from sklearn import svm
from random import shuffle
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from math import log
from sklearn.model_selection import KFold
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split



df = pd.read_csv('merge.csv', encoding = 'utf-8')
countries_in_edu = df[df.columns.values[0]].values
X = df[df.columns.values[1:]].values
Y = []
dic ={}
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
	if df1.iloc[j,-1]=='Developing':
		dic[i]=0
	elif df1.iloc[j,-1]=='Developed':
		dic[i]=1

for i in countries_in_edu:
	Y.append(dic[i])

test_size=0.3
training_data_x, validation_x, training_data_y, validation_y = train_test_split(X,Y, test_size=test_size, random_state=7)

clf = BaggingClassifier(tree.DecisionTreeClassifier(),max_samples=0.8)
clf = clf.fit(training_data_x, training_data_y)




count = 0
correct = 0
for i in xrange(len(validation_x)):
	an = clf.predict([validation_x[i]])[0]
	if an==validation_y[i]:
		correct+=1
	count+=1
print correct*100/count

	
