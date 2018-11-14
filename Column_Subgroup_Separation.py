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
		# print subgroups
		indexes = set(df['Country or Area'])
		df_new = pd.DataFrame(inlsdex = range(len(indexes)))
		# print df_new
		count = 0
		print file
		columns =  df.columns.values
		for subgroup in subgroups:
			df2 = df.loc[df["Subgroup"]==subgroup]
			if count==0:
				df3 = df.loc[df["Subgroup"]==subgroup]["Country or Area"].reset_index(drop=True)
				# print df3
				df_new = pd.concat([df_new, df3], axis=1)
				count = count +1
			df2 =df2.reset_index(drop=True)
			df2 = df2[[columns[2]]]
			new_column = subgroup + " "+ columns[2]
			df2.columns = [new_column]
			df_new = pd.concat([df_new, df2], axis=1)
		# print df_new
		new_path = "./newdata/rr/" + file
		df_new.to_csv(new_path,index=False)
			# break
if __name__ == '__main__':
	func()