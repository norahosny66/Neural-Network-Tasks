import random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class IrisDataset:
    filepath = 'IrisData.txt'
    dataSet = pd.read_csv(filepath, ',')

    @staticmethod
    def Train_Test_Splite():
        IrisSetosa = np.array(IrisDataset.dataSet.iloc[0:50,:-1].values.tolist())
        IrisVersicolor = np.array(IrisDataset.dataSet.iloc[50:100,:-1].values.tolist())
        IrisVirginica = np.array(IrisDataset.dataSet.iloc[100:150,:-1].values.tolist())

        x_train1, x_test1 = train_test_split(IrisSetosa, train_size=0.6,shuffle=True)
        x_train2, x_test2 = train_test_split(IrisVersicolor, train_size=0.6,shuffle=True)
        x_train3, x_test3 = train_test_split(IrisVirginica, train_size=0.6,shuffle=True)
        x_train = np.concatenate([x_train1 , x_train2,x_train3])
        x_test = np.concatenate([x_test1 , x_test2 , x_test3])

        y_train = np.concatenate([ np.full((30,3), [1,0,0]), np.full((30,3), [0,1,0]),np.full((30,3), [0,0,1])])
        y_test =  np.concatenate([ np.full((20,3), [1,0,0]), np.full((20,3), [0,1,0]),np.full((20,3), [0,0,1])])

        return x_train, y_train, x_test, y_test
