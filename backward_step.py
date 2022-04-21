import numpy as np
from ForwardStep import *


def encode(y):
    mx = max(y)
    encoded_y = []
    for i in range(len(y)):
        if y[i] < mx:
            encoded_y.append(0)
        else:
            encoded_y.append(1)
    return encoded_y


def sigmoid_drev(net):
    return np.array(net) * (1 - np.array(net))


def hyperbolic_tangent_drev(net):
    return 1 - (np.array(net) ** 2)


def activation_check(net, activation_type):
    if activation_type == "Sigmoid":
        return sigmoid_drev(net)
    return hyperbolic_tangent_drev(net)


def backward(all_weights, all_nets, actual_output, activation_fn):
    all_nets.reverse()
    all_weights.reverse()

    all_signal_error = []
    for layer_index in range(len(all_nets)):
        if layer_index == 0:  # last layer
            last_layer_encoded_nets = encode(all_nets[layer_index])
        layer_signal_error = []

        for neuron in range(len(all_nets[layer_index])):

            if layer_index == 0:  # last layer
                neuron_error = ( actual_output[neuron]-all_nets[layer_index][neuron] ) * activation_check(
                    all_nets[layer_index][neuron], activation_fn)
            else:  # hidden layers
                if neuron == 0: continue
                x = all_weights[layer_index-1].T[neuron]
                y = all_signal_error[layer_index - 1]
                neuron_error = np.dot(x, y) * activation_check(all_nets[layer_index][neuron], activation_fn)
            layer_signal_error.append(neuron_error)

        all_signal_error.append(layer_signal_error)

    all_nets.reverse()
    all_weights.reverse()
    return all_signal_error


def update_weights(all_weights, all_signal_error, all_nets, sample, learning_rate):
    all_updated_weights = []
    all_signal_error.reverse()

    for layer_index in range(len(all_weights)):
        update_layer_weights = []
        for neuron in range(len(all_weights[layer_index])):
            if layer_index == 0:  # use features (x)
                update_weight = all_weights[layer_index][neuron] + (
                        learning_rate * all_signal_error[layer_index][neuron] * sample)
            else:  # use nets
                x = np.array(all_nets[layer_index - 1])
                update_weight = all_weights[layer_index][neuron] + (
                        learning_rate * all_signal_error[layer_index][neuron] * x)
            update_layer_weights.append(update_weight)
        update_layer_weights = np.array(update_layer_weights)
        all_updated_weights.append(update_layer_weights)
    return all_updated_weights

    print("AllUpdatedWeights:")
    print(all_updated_weights)
