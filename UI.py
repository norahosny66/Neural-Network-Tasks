from matplotlib.figure import Figure
from UI_Attributes import *
from Model import *


def SwitchFrame(frame1, frame2):
    frame1.pack_forget()
    frame2.pack(fill=BOTH, expand=1)


def Bind_Feature1(event):
    selected_feature2.set(" ")
    features_list2 = [x for x in Features_list if not x in [selected_feature1.get()]]
    feature1_cb2['values'] = features_list2


def Bind_Class1(event):
    selected_class2.set(" ")
    Class_list2 = [x for x in Class_list if not x in [selected_class1.get()]]
    class2_cb['values'] = Class_list2


def UserInputFrameBuilder():
    feature1_cb.bind('<<ComboboxSelected>>', Bind_Feature1)
    class1_cb.bind('<<ComboboxSelected>>', Bind_Class1)
    TrainButton['command'] = lambda: TrainClick()
    SwitchButtonUser['command'] = lambda: SwitchFrame(User_Input_frame, Plotting_frame)
    SwitchButtonPlotting['command'] = lambda: SwitchFrame(Plotting_frame, User_Input_frame)


def return_user_input():
    return selected_class1.get(), selected_class2.get(), selected_feature1.get(), selected_feature2.get(), LR.get(), Threshold.get(),Epochs.get(), bias_selection.get()


def TrainClick():
    class1, class2, feature1, feature2, learningRate, Threshold,Epochs, isBias = return_user_input()
    Dataset1 = IrisDataset.GetDataSet(class1, [feature1, feature2])
    Dataset2 = IrisDataset.GetDataSet(class2, [feature1, feature2])

    x_train, y_train, x_test, y_test = IrisDataset.Train_Test_Splite(Dataset1, Dataset2)

    model = AdalineModel()
    model.fit(x_train, y_train, isBias, learningRate, Threshold,Epochs)

    # plotting
    fig = Figure(figsize=(5, 5))
    ax = fig.subplots()
    ax.scatter(Dataset1.values[:, 0], Dataset1.values[:, 1], label=class1, c='blue')
    ax.scatter(Dataset2.values[:, 0], Dataset2.values[:, 1], label=class2, c='red')
    ax.set_xlabel(feature1)
    ax.set_ylabel(feature2)
    Xpoint = [min(x_train[:, 0]), max(x_train[:, 0])]
    ax.plot(Xpoint, model.GetPoints(Xpoint))
    ax.legend(loc='upper left')
    canvas = FigureCanvasTkAgg(fig, User_Input_frame)
    canvas.get_tk_widget().place(x=20, y=350)

    # test
    y_pred = model.predict(x_test)

    #print(y_pred)
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

    print("bias ",model.weight[0][0])
    # display theta
    Decisionline= str(format(model.weight[1][0],".3f")+" X1 + ") +str(format(model.weight[2][0],".3f")+" X2 + ")+str(format(model.weight[0][0],".3f")+" =0 ")
    WightsLable.config(text='Decision line :' + str(Decisionline))

def UI_Controller():
    # build user input frame
    UserInputFrameBuilder()
    # set plotting frame as initial scene
    Plotting_frame.pack(fill=BOTH, expand=1)
    t.mainloop()
