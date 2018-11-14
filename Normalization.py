import os 
import sys
import pandas as pd
import csv
import re
import numpy as np
from sklearn import preprocessing

def function():
	path = "./Final_Education.csv"
	df = pd.read_csv(path)
	columns = df.columns.values
	columns = columns[1:]	

	print columns
	for column in columns:
		feature_list = df[column]
		minimum = min(feature_list)
		maximum = max(feature_list)
		df[column] = (df[column]-minimum)/(maximum-minimum)
	print df
	store_path = "./Final_Education_Normalization.csv"
	df.to_csv(store_path, index=False)

if __name__ == '__main__':
	function()