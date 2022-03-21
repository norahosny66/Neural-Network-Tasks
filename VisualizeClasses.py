from matplotlib import pyplot as plt
import numpy as np
from ReadDataset import *
colors = ['blue', 'red']
Class_names = ['Iris-setosa','Iris-versicolor','Iris-virginica']
Class_Index =dict({"Iris-setosa": [0,50], "Iris-versicolor": [50,100], "Iris-virginica": [100,150]})
def Plot_2_Classes(Feature1,Feature2,Class1,Class2):
       start_index = Class_Index[Class1][0]
       end_index = Class_Index[Class1][1]
       plt.scatter(Feature1[start_index: end_index ], Feature2[start_index: end_index],label=Class1, c='blue')
       start_index=Class_Index[Class2][0]
       end_index+=Class_Index[Class2][1]
       plt.scatter(Feature1[start_index: end_index], Feature2[start_index: end_index], label=Class2, c='red')

       plt.legend(loc='upper left')
       plt.show()