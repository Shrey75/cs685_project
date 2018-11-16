import os 
import sys
import pandas as pd
import csv
from sklearn.cluster import KMeans
import numpy as np 
import matplotlib.pyplot as plt 
import pickle as pkl
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
import re

df = pd.read_csv("./Final_Education_Normalization.csv")
cols = df.columns.values
X = df[cols[1:]].values
# feature_arr_male = []
# feature_arr_female = []
# for i in range(len(columns)):
# 	if "Male" in columns[i]:
# 		feature_arr_male.append(columns[i])
# for i in range(len(columns)):
# 	if "Female" in columns[i]:
# 		feature_arr_female.append(columns[i])


df = pd.read_csv("health.csv")
features = list(df.columns.values[1:])
for i in features:
	if re.search('19',i) or re.search('_19',i):
		features.remove(i)

for i in features:
	Y = df[i].values
	LR = LinearRegression()
	model = LR.fit(X, Y)
	# model1 = MLPRegressor(hidden_layer_sizes=(30,14), learning_rate_init=0.00004,max_iter=400000, early_stopping=True)
	# model1 =model1.fit(objective1,y1)
	# arr = np.argsort(model1.coef_)[::-1][:3]
	# print  [feature_arr_male[i] for i in arr ]
	# print len(feature_arr_male)
	predications = model.predict(X)
	# print literacy_male_predications, y_test1
	if r2_score(Y,predications)>0.75:
		print i+'  &  '+str(round(r2_score(Y,predications),3))+'   \\\\ \\hline'

