from matplotlib.figure import Figure
from UI_Attributes import *
from Model import *


def SwitchFrame(frame1, frame2):
    frame1.pack_forget()
    frame2.pack(fill=BOTH, expand=1)



def UserInputFrameBuilder():

    TrainButton['command'] = lambda: TrainClick()



def return_user_input():
    return HiddenLayers.get(),Neurons.get(), LR.get(),Epochs.get(),selected_Activation_fn.get(), bias_selection.get()

def TrainClick():
    HiddenLayers, Neurons, learningRate, feature2, Epochs, selected_Activation_fn,isBias = return_user_input()

    Dataset1=1
    Dataset2=2
    x_train, y_train, x_test, y_test = IrisDataset.Train_Test_Splite(Dataset1, Dataset2)

    model = AdalineModel()
    #model.fit(x_train, y_train, isBias, learningRate, Threshold,Epochs)

    # plotting
    fig = Figure(figsize=(5, 5))
    ax = fig.subplots()
   # ax.scatter(Dataset1.values[:, 0], Dataset1.values[:, 1], label=class1, c='blue')
   # ax.scatter(Dataset2.values[:, 0], Dataset2.values[:, 1], label=class2, c='red')
   # ax.set_xlabel(feature1)
    ax.set_ylabel(feature2)
    Xpoint = [min(x_train[:, 0]), max(x_train[:, 0])]
    ax.plot(Xpoint, model.GetPoints(Xpoint))
    ax.legend(loc='upper left')
    canvas = FigureCanvasTkAgg(fig, User_Input_frame)
    canvas.get_tk_widget().place(x=20, y=350)

    # test
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
    WightsLable.config(text='Decision line : {:.2f} X1 + {:.2f} X2 + {:.2f} = 0 '.format(model.weight[1][0], model.weight[2][0], model.weight[0][0]))


def UI_Controller():
    # build user input frame
    UserInputFrameBuilder()
    # set plotting frame as initial scene
    User_Input_frame.pack(fill=BOTH, expand=1)
    t.mainloop()
