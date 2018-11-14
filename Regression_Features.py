import os 
import sys
import pandas as pd
import csv
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 
import pickle as pkl
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
def func():
	path = "./Final_Education.csv"
	df = pd.read_csv(path)
	columns = df.columns.values
	feature_arr_male = []
	feature_arr_female = []
	for i in range(len(columns)):
		if "Male" in columns[i]:
			feature_arr_male.append(columns[i])
	for i in range(len(columns)):
		if "Female" in columns[i]:
			feature_arr_female.append(columns[i])
	male_literacy = "Male 15-24 yr Literacy rate of 15-24 year-olds"
	female_literacy = "Female 15-24 yr Literacy rate of 15-24 year-olds"
	feature_arr_female.remove("Female 15-24 yr Literacy rate of 15-24 year-olds")
	feature_arr_male.remove("Male 15-24 yr Literacy rate of 15-24 year-olds")

	#Precdiction of Literacy for male
	LR1 = LinearRegression()
	objective1 = df[feature_arr_male[:]]
	y1 = df[male_literacy]
	# print y1
	X_train1, X_test1, y_train1, y_test1 = train_test_split(objective1, y1, test_size=0.1)
	model1 = LR1.fit(X_train1, y_train1)
	literacy_male_predications = model1.predict(X_test1)
	print literacy_male_predications, y_test1
	print r2_score(y_test1,literacy_male_predications)


	#Precdiction of Literacy for Female
	LR2 = LinearRegression()
	objective2 = df[feature_arr_female[:]]
	y2 = df[female_literacy]
	# print y1
	X_train2, X_test2, y_train2, y_test2 = train_test_split(objective2, y2, test_size=0.1)
	model2 = LR2.fit(X_train2, y_train2)
	literacy_female_predications = model2.predict(X_test2)
	print literacy_female_predications, y_test2
	print r2_score(y_test2,literacy_female_predications)



if __name__ == '__main__':
	func()