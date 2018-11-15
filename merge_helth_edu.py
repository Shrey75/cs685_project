from sklearn.decomposition import PCA
import pandas as pd 
from sklearn.feature_selection import VarianceThreshold
import numpy as np


df_new = pd.DataFrame()
for i, file in enumerate(["Final_Education_Normalization.csv","health_Normalization.csv"]):
	print file
	df = pd.read_csv(file)
	if i==0:
		df_new = df
	else:
		del df[df.columns.values[0]]
		df_new = pd.concat([df_new, df], axis=1)
		
new_path = "./merge.csv"
df_new.to_csv(new_path, index = False)