import numpy as np
import pandas as pd


class AdalineModel:

    def fit(self, x, y, isBias, learningRate, Threshold):
        self.weight = np.random.rand(3, 1)
        if not isBias:
            self.weight[0] = 0
        while True:
            i = 0

            for x1, x2 in x:

                v = self.weight[0][0] + self.weight[1][0] * x1 + self.weight[2][0] * x2
                if v <0:
                    v = 0
                else:
                    v = 1
                error = y[i][0]-v

                if isBias:
                    self.weight[0] = self.weight[0] + error * learningRate
                self.weight[1] = self.weight[1] + error * learningRate * x1
                self.weight[2] = self.weight[2] + error * learningRate * x2
                i += 1

            sum = 0
            i=0
            for x1, x2 in x:
                v = self.weight[0][0] + self.weight[1][0] * x1 + self.weight[2][0] * x2
                if v < 0:
                    v = 0
                else:
                    v = 1
                error = y[i][0]-v
                sum += (error * error)
                i += 1
            msq = sum / (2 * x.shape[0])
            print(msq,x.shape[0])
            if msq < Threshold:
                break


    def predict(self , x):
        y = []
        for x1, x2 in x:
            v = self.weight[0][0] + self.weight[1][0] * x1 + self.weight[2][0] * x2
            if v < 0:
                y.append(0)
            else:
                y.append(1)

        return y

    def ConfusionMatrix(self, Y, y_pred):
        FP = 0
        FN = 0
        TP = 0
        TN = 0
        for i in range(len(Y)):
            if Y[i][0] == 1 and y_pred[i] == 1:
                TP += 1
            elif Y[i][0] == 0 and y_pred[i] == 1:
                FP += 1
            elif Y[i][0] == 1 and y_pred[i] == 0:
                FN += 1
            elif Y[i][0] == 0 and y_pred[i] == 0:
                TN += 1
        return TP, FP, TN, FN

    def GetPoints(self, X):
        Y = []
        for x1 in X:
            Y.append((-self.weight[0] - self.weight[1] * x1) / self.weight[2])
        return Y
