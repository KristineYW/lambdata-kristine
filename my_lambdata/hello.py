# Import enlarge function
from my_mod import split, date_split
from pandas import DataFrame
from scikit-learn.model_selection import train_test_split


df = DataFrame({'state':['CT','CO','CA','TX']})
print(df.head())

# Invoke split
split(df)

# Invoke date_split function
date_split()
