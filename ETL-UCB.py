import pandas as pd
import numpy as np 
# Extraction
wine_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
wine_data = pd.read_csv(wine_url, header=None)
wine_quality_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine_quality_data = pd.read_csv(wine_quality_url, sep= ";")
print(wine_data.head())
print(wine_quality_data.head())
wine_data.to_csv('wine_dataset.csv',index=False)
wine_quality_data.to_csv('wine_quality_dataset.csv',index=False) 