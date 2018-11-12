import os 
import sys
import pandas as pd
import csv
import re
import numpy as np

def function():
	df_new = pd.DataFrame()
	path = "./newdata/education3/"
	for i, file in enumerate(os.listdir(path)):
		path1 = path + file
		df = pd.read_csv(path1)
		if i==0:
			df_new = df
		else:
			del df["Country or Area"]
			df_new = pd.concat([df_new, df], axis=1)
			
	new_path = "./Final_Education.csv"
	df_new.to_csv(new_path, index = False)

if __name__ == '__main__':
	function()