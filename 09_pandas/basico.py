import pandas as pd

# crea un data set simple

data= {'Name':["Jhon","Anna","Peter","Linda"],
       'Location':["EU","Paris","Berlin","London"],
       'Age' : [24,23,12,33]}


data_pandas= pd.DataFrame(data)

print(data_pandas)

#separar dados

print(data_pandas[data_pandas.Age>30])
