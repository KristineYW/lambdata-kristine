# Import enlarge function
from my_mod import df_split, date_split
import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split


df = DataFrame({'state': ['CT', 'CO', 'CA', 'TX']})
print(df.head())

# Invoke split
df_split()

# Invoke date_split function
date_split()
