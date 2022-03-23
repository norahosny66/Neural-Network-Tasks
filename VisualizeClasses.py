from itertools import combinations
from IrisDataset import *
from matplotlib.figure import Figure


def Plot_2_Classes():
    fig = Figure(figsize=(6, 6))
    feature_index = dict({0: "X1", 1: "X2", 2: "X3", 3: "X4"})
    six_combinations = list(combinations(feature_index.keys(), 2))

    single_plot_index = 1
    for x in six_combinations:
        Class1 = IrisDataset.GetDataSet('Iris-setosa', [feature_index[x[0]], feature_index[x[1]]]).values
        Class2 = IrisDataset.GetDataSet('Iris-versicolor', [feature_index[x[0]], feature_index[x[1]]]).values
        Class3 = IrisDataset.GetDataSet('Iris-virginica', [feature_index[x[0]], feature_index[x[1]]]).values
        ax = fig.add_subplot(2, 3, single_plot_index)
        ax.scatter(Class1[:, 0], Class1[:, 1], label='Iris-setosa', c='blue')
        ax.scatter(Class2[:, 0], Class2[:, 1], label='Iris-versicolor', c='red')
        ax.scatter(Class3[:, 0], Class3[:, 1], label='Iris-virginica', c='green')
        ax.legend(loc='upper left')
        ax.set_xlabel(feature_index[x[0]])
        ax.set_ylabel(feature_index[x[1]])
        single_plot_index += 1
    return fig
