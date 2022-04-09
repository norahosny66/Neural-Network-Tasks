import random

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class IrisDataset:
    filepath = 'IrisData.txt'
    dataSet = pd.read_csv(filepath, ',')
    co = 0

    @staticmethod
    def GetDataSet(ClassName, Colms):
        if ClassName == 'Iris-setosa':
            return IrisDataset.dataSet[0:50][Colms]
        elif ClassName == 'Iris-versicolor':
            return IrisDataset.dataSet[50:100][Colms].reset_index(drop=True)
        else:
            return IrisDataset.dataSet[100:150][Colms].reset_index(drop=True)

    @staticmethod
    def Train_Test_Splite(Dataset1, Dataset2):
        Dataset1 = np.array(Dataset1.values.tolist())
        Dataset2 = np.array(Dataset2.values.tolist())
        x_train1, x_test1 = train_test_split(Dataset1, train_size=0.6)
        x_train2, x_test2 = train_test_split(Dataset2, train_size=0.6)
        x_train = np.concatenate([x_train1, x_train2])
        x_test = np.concatenate([x_test1, x_test2])
        y_train = np.concatenate([np.zeros((30, 1)), np.ones((30, 1))]) * 2 - 1
        y_test = np.concatenate([np.zeros((20, 1)), np.ones((20, 1))]) * 2 - 1


        p = np.random.permutation(len(y_train))
        x_train = x_train[p]
        y_train = y_train[p]

        return x_train, y_train, x_test, y_test
