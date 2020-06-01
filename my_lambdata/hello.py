# Import enlarge function
from my_lambdata.my_mod import enlarge
from pandas import DataFrame

print ("HELLO")

# Invoke enlarge()
print(enlarge(8))

df = DataFrame({'state':['CT','CO','CA','TX']})
print(df.head())