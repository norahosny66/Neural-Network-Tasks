from tkinter import *
from tkinter.ttk import Combobox
root = Tk()
root.geometry('800x500')

Features_list=["X1","X2","X3","X4"]
selected_feature1 = StringVar()
selected_feature2 = StringVar()

Class_list=['Iris-setosa','Iris-versicolor','Iris-virginica']
selected_class1 = StringVar()
selected_class2 = StringVar()

bias_selection = IntVar()
def Bind_Feature1(event):
    features_list2 = [x for x in Features_list if not x in [selected_feature1.get()]]
    features2_cb = Combobox(root, values=features_list2, textvariable=selected_feature2).place(x=200, y=100)
    features2_label = Label(root, text="Feature 2", height = 1, width = 7)
    features2_label.place(x=100,y=100)

def UserInput ():
 feature1_cb = Combobox(root, values=Features_list, textvariable=selected_feature1)
 feature1_cb.place(x=200,y=70)
 feature1_label = Label(root, text = "Feature 1",   height = 1, width = 7)
 feature1_label.place(x=100,y=70)
 feature1_cb.bind('<<ComboboxSelected>>', Bind_Feature1)

 class1_cb = Combobox(root, values=Class_list, textvariable=selected_class1)
 class1_cb.place(x=200, y=10)
 class1_label = Label(root, text="Class 1", height=1, width=7).place(x=100, y=10)
 class1_cb.bind('<<ComboboxSelected>>', Bind_Class1)

 learning_rate = Text(root, height=1, width=7)
 learning_rate.place(x=200,y=150)
 learning_rate_value = learning_rate.get("1.0", "end-1c")
 learning_rate_label = Label(root, text="Learning rate", height=1, width=10).place(x=100,y=150)

 epochs = Text(root, height=1, width=7)
 epochs.place(x=200, y=180)
 epochs_label = Label(root, text="epochs number", height=1, width=12).place(x=100, y=180)
 epochs_value = epochs.get("1.0", "end-1c")

 Bias_CheckBox = Checkbutton(root, text=' Add Bias ', variable=bias_selection, onvalue=1, offvalue=0)
 Bias_CheckBox  .place(x=200,y=220)

 root.mainloop()
 return selected_feature1.get(),selected_feature2.get(),selected_class1.get(),selected_class2.get(),learning_rate_value,epochs_value

def Bind_Class1(event):
    Class_list2 = [x for x in Class_list if not x in [selected_class1.get()]]
    class2_cb = Combobox(root, values=Class_list2, textvariable=selected_class2).place(x=200, y=40)
    class2_label = Label(root, text="Class 2", height = 1, width = 7)
    class2_label.place(x=100,y=40)



