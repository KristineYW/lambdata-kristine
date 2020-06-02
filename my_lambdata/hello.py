# Import enlarge function
from my_mod import split, date_split
from pandas import DataFrame



df = DataFrame({'state':['CT','CO','CA','TX']})
print(df.head())

# Invoke split
split(df)

# Invoke date_split function
date_split()
