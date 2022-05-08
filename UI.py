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
    all_train_samples = []
    for epoch in range(Epochs):
        for sample in range(len(x_train)):
            allnets = forward(x_train[sample], isBias, AllWeights, ActivationFn)
            if epoch == Epochs - 1:
                encoded_train = backward_step.encode(allnets[-1])
                all_train_samples.append(encoded_train)
            signal_error = backward_step.backward(AllWeights, allnets, y_train[sample], ActivationFn)
            AllWeights = backward_step.update_weights(AllWeights, signal_error, allnets, x_train[sample], learningRate)
    all_train_samples = np.array(all_train_samples)


    # Test
    all_pred_samples = []
    for sample in range(len(x_test)):
        encoded_out = test.testt(x_test[sample], isBias, AllWeights, ActivationFn)
        all_pred_samples.append(encoded_out)
    all_pred_samples = np.array(all_pred_samples)

 #accuracy
    Train_accuracy = metrics.accuracy_score(y_train, all_train_samples) * 100
    print("Train Accuracy ", Train_accuracy)
    Test_accuracy = metrics.accuracy_score(y_test, all_pred_samples) * 100
    print("Test Accuracy ", Test_accuracy)

#confusion
    y_test=encoded_to_labels(y_test)
    all_pred_samples=encoded_to_labels(all_pred_samples)
    print(metrics.confusion_matrix(y_test, all_pred_samples,labels=["Setosa","Versi_Color","Virginica"]))
    # Printing the precision and recall, among other metrics
    print(metrics.classification_report(y_test, all_pred_samples,labels=["Setosa","Versi_Color","Virginica"]))


def encoded_to_labels(y):
    y_label = []
    for sample in y:
        if (sample == np.array([1, 0, 0])).all():
            y_label.append("Setosa")
        elif (sample == np.array([0, 1, 0])).all():
            y_label.append("Versi_Color")
        else:
            y_label.append("Virginica")
    return y_label



def UI_Controller():
    # build user input frame
    UserInputFrameBuilder()
    # set plotting frame as initial scene
    User_Input_frame.pack(fill=BOTH, expand=1)
    t.mainloop()
