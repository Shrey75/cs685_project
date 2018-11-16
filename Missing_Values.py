import os 
import sys
import pandas as pd
import csv

def func():
	path = "./newdata/rr/"
	for file in os.listdir(path):
		path1 = path+file
		df = pd.read_csv(path1)
		if len(df.columns.values)==2:
			continue
		subgroups = set(df['Subgroup'])
		country = df["Country or Area"]
		distinct = set(country)
		print df.shape
		for country in distinct:
			df2 = df.loc[df["Country or Area"]==country]
			sg = df2["Subgroup"]
			sg= sg.values
			# print sg
			to_add = list(subgroups.symmetric_difference(sg))
			# print to_add
			for value in to_add:
				df.loc[-1] = [country, value, 0]
				df.index = df.index +1
				df = df.sort_index()
		new_path = "./newdata/rr/" + file
		df.to_csv(new_path,index=False)
		# print df.shape, "yeah", subgroups, file
			# break
		# break

if __name__ == '__main__':
	func()
