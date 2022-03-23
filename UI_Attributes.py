from tkinter import *
import tkinter as t
from tkinter.ttk import *

root = Tk()
root.geometry('1200x900')

Plotting_frame = t.Frame(root, background="snow")
User_Input_frame = t.Frame(root, background="snow")

Features_list=["X1","X2","X3","X4"]
selected_feature1 = StringVar()
selected_feature2 = StringVar()
feature1_cb = Combobox(User_Input_frame, values=Features_list, textvariable=selected_feature1)
feature1_label = Label(User_Input_frame, text="Feature 1")
features2_label = Label(User_Input_frame, text="Feature 2")

Class_list=['Iris-setosa','Iris-versicolor','Iris-virginica']
selected_class1 = StringVar()
selected_class2 = StringVar()
class1_cb = Combobox(User_Input_frame, values=Class_list, textvariable=selected_class1)
class1_label = Label(User_Input_frame, text="Class 1").place(x=100, y=10)

bias_selection = IntVar()

epochs_number=StringVar()
epochs = t.ttk.Entry(User_Input_frame, width = 10, textvariable = epochs_number)
epochs_label = Label(User_Input_frame, text="epochs number",  width=15).place(x=100, y=180)
LR=StringVar()
learning_rate = t.ttk.Entry(User_Input_frame, width = 10, textvariable = LR)
learning_rate_label = Label(User_Input_frame, text="Learning rate",  width=15).place(x=100,y=150)

Bias_CheckBox = Checkbutton(User_Input_frame, text=' Add Bias ', variable=bias_selection, onvalue=1, offvalue=0)