import numpy as np
import pandas as pd


class IrisDataset:

    def __init__(self):
        filepath = 'IrisData.txt'
        self.dataSet = pd.read_csv(filepath, ',')

    def GetDataSet(self, ClassName, Colms):
        if ClassName == 'Iris-setosa':
            return self.dataSet[0:50][Colms]
        elif ClassName == 'Iris-versicolor':
            return self.dataSet[50:100][Colms].reset_index(drop=True)
        else:
            return self.dataSet[100:150][Colms].reset_index(drop=True)

    def Train_Test_Splite(self, Dataset1, Dataset2):
        Dataset1 = np.array(Dataset1.values.tolist())
        Dataset2 = np.array(Dataset2.values.tolist())
        x_train1, x_test1, tmp = np.split(Dataset1, [30, 50])
        x_train2, x_test2, tmp = np.split(Dataset2, [30, 50])
        x_train = np.concatenate([x_train1, x_train2])
        x_test = np.concatenate([x_test1, x_test2])
        y_train = np.concatenate([np.zeros((30, 1)), np.ones((30, 1))]) * 2 - 1
        y_test = np.concatenate([np.zeros((20, 1)), np.ones((20, 1))]) * 2 - 1

        return x_train, y_train, x_test, y_test
