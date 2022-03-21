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
