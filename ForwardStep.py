import numpy as np
import pandas as pd

import backward_step
from IrisDataset import *

'''
Initialize random weights
'''


def CreateWeightMatrix(hiddenlayers, neurons):
    AllWeights = []
    AllWeights.append(np.random.rand(neurons[0], 5).round(3))
    for i in range(hiddenlayers - 1):
        AllWeights.append(np.random.rand(neurons[i + 1], neurons[i] + 1).round(3))
    AllWeights.append(np.random.rand(3, neurons[-1] + 1).round(3))
    return AllWeights


def Sigmoid(v):
    return 1 / (1 + np.exp(-v))


def HyperbolicTangent(v):
    return (1 - np.exp(-v)) / (1 + np.exp(-v))


def forward(x, isBias, AllWeights, Sample, ActivitionFn):
    AllLayersOutput = []

    if isBias:
        x = np.insert(x, 0, 1, axis=1)
    else:
        x = np.insert(x, 0, 0, axis=1)

    for layer in range(0, len(AllWeights)):
        LayerOutput = []

        if isBias and layer != len(AllWeights) - 1:
            LayerOutput.append(1)
        elif not isBias and layer != len(AllWeights) - 1:
            LayerOutput.append(0)

        for neuron in range(len(AllWeights[layer])):
            if layer == 0:
                neuron_net = np.dot(x[0], AllWeights[layer][neuron])
            else:
                neuron_net = np.dot(AllLayersOutput[layer - 1], AllWeights[layer][neuron])

            if ActivitionFn == Sigmoid:
                LayerOutput.append(Sigmoid(neuron_net).round(3))
            else:
                LayerOutput.append(HyperbolicTangent(neuron_net).round(3))
        AllLayersOutput.append(LayerOutput)

    print("features:")
    print(x[0])
    print("AllWeights:")
    print(AllWeights)
    # print(AllWeights[1].T[0])
    print("AllNets:")
    print(AllLayersOutput)
    all_error = backward_step.backward(AllWeights, AllLayersOutput, np.array([1, 0, 0]), "Sigmoid")

    backward_step.update_weights(AllWeights, all_error, AllLayersOutput, x[0], 0.1)

