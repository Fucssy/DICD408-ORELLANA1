import pandas as pd
import numpy as np 
# Extraction
wine_url = "ebrios.csv"
wine_url = pd.read_csv(wine_url, sep= ";")
print(wine_url.head())
