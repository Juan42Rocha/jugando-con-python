from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

iris_dataset = load_iris()


print("Claves de  iris_dataset: \n",format(iris_dataset.keys() )+ "\n..." )


print("Descrition: \n",iris_dataset['DESCR'][193:]+"\n...")

print("Target nanes: \n",format(iris_dataset['target_names'])+"\n...")

print("Fuature names: \n{}",format(iris_dataset['feature_names'])+"\n...")

print("Type of data: \m", format(iris_dataset['data'][5:])+"\n...")

print("Target code: \n", format([iris_dataset['target']])+"\n...")


X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'],iris_dataset['target'], random_state=0)



#Crea dataframe
iris_dataframe = pd.DataFrame(X_train, columns= iris_dataset.feature_names)

#Crea a scatter matrix from the DataFrame, color by y_train
grr = pd.plotting.scatter_matrix(iris_dataframe,c=y_train, figsize=(15,15))

plt.show()
