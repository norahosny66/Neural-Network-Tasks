import numpy as np
import pandas as pd


class PerceptronModel:

    def fit(self, x, y, isBias, learningRate, epochs):
        self.weight = np.random.rand(3, 1)
        if not isBias:
            self.weight[0] = 0
        for t in range(epochs):
            i = 0
            for x1, x2 in x:
                v = self.weight[0] + self.weight[1] * x1 + self.weight[2] * x2
                d = np.sign(v)
                error = d - y[i]
                if isBias:
                    self.weight[0] = self.weight[0] - error * learningRate
                self.weight[1] = self.weight[1] - error * learningRate * x1
                self.weight[2] = self.weight[2] - error * learningRate * x2
                i += 1

    def predict(self, x):
        y = []
        for x1, x2 in x:
            v = self.weight[0] + self.weight[1] * x1 + self.weight[2] * x2
            y.append(np.sign(v))

        return y

    def ConfusionMatrix(self, Y, y_pred):
        FF = 0
        FP = 0
        PF = 0
        PP = 0
        for i in range(len(Y)):
            if Y[i] == 1 and y_pred == 1:
                PP += 1
            elif Y[i] == -1 and y_pred == 1:
                FP += 1
            elif Y[i] == 1 and y_pred == -1:
                PF += 1
            elif Y[i] == -1 and y_pred == -1:
                FF += 1
        return FF, FP, PF, PP
