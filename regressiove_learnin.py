from sklearn.decomposition import PCA
import pandas as pd 
from sklearn.feature_selection import VarianceThreshold
import numpy as np

df = pd.read_csv("Final_Education_Normalization.csv",encoding = 'utf-8')
cols = df.columns.values
rows = df.index.values
print cols