from matplotlib.figure import Figure
from UI_Attributes import *
from sklearn import metrics
from ForwardStep import *
from test import *


def UserInputFrameBuilder():
    TrainButton['command'] = lambda: TrainClick()


def return_user_input():
    return HiddenLayers.get(), Neurons.get(), LR.get(), Epochs.get(), selected_Activation_fn.get(), bias_selection.get()


def TrainClick():
    HiddenLayers, Neurons, learningRate, Epochs, ActivationFn, isBias = return_user_input()
    neurons = []
    for i in range(HiddenLayers):
        neurons.append(int(Neurons.split(',')[i]))

    x_train, y_train, x_test, y_test = IrisDataset.Train_Test_Splite()
    AllWeights = CreateWeightMatrix(HiddenLayers, neurons)
    wibhhndbj = AllWeights
    if isBias:
        x_train = np.insert(x_train, 0, 1, axis=1)
        x_test = np.insert(x_test, 0, 1, axis=1)
    else:
        x_train = np.insert(x_train, 0, 0, axis=1)
        x_test = np.insert(x_test, 0, 0, axis=1)

    for epoch in range(Epochs):
        for sample in range(len(x_train)):
            allnets = forward(x_train[sample], isBias, AllWeights, ActivationFn)
            signal_error = backward_step.backward(AllWeights, allnets, y_train[sample], ActivationFn)
            AllWeights = backward_step.update_weights(AllWeights, signal_error, allnets, x_train[sample], learningRate)

    # Test
    all_pred_samples = []
    for sample in range(len(x_test)):
        encoded_out = test.testt(x_test[sample], isBias, AllWeights, ActivationFn)
        all_pred_samples.append(encoded_out)

    all_pred_samples = np.array(all_pred_samples)
    print(all_pred_samples)
    accuracy = metrics.accuracy_score(y_test, all_pred_samples)
    print(accuracy)


'''''
    y_pred = model.predict(x_test)

    TP, FP, TN, FN = model.ConfusionMatrix(y_test, y_pred)
    test_accuracy = (TN + TP) / (TN + TP + FN + FP)
    TP2, FP2, TN2, FN2 = model.ConfusionMatrix(y_train, model.predict(x_train))
    train_accuracy = (TP2 + TN2) / (TN2 + FP2 + FN2 + TP2)

    # plotting ConfusionMatrix
    Testlable.config(text='Test')
    TestFFlable.config(text='TP : ' + str(TP))
    TestFPlable.config(text='FP : ' + str(FP))
    TestPFlable.config(text='TN : ' + str(TN))
    TestPPlable.config(text='FN : ' + str(FN))
    TestAccLable.config(text='Accuracy : ' + str(test_accuracy * 100) + '%')

    Trainlable.config(text='Train')
    TrainFFlable.config(text='TP : ' + str(TP2))
    TrainFPlable.config(text='FP : ' + str(FP2))
    TrainPFlable.config(text='TN : ' + str(TN2))
    TrainPPlable.config(text='FN : ' + str(FN2))
    TrainAccLable.config(text='Accuracy : ' + str(train_accuracy * 100) + '%')
    
     # display theta
    #WightsLable.config(text='Decision line : {:.2f} X1 + {:.2f} X2 + {:.2f} = 0 '.format(model.weight[1][0], model.weight[2][0], model.weight[0][0]))
'''


def UI_Controller():
    # build user input frame
    UserInputFrameBuilder()
    # set plotting frame as initial scene
    User_Input_frame.pack(fill=BOTH, expand=1)
    t.mainloop()
