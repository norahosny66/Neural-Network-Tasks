from tkinter import *
import tkinter as t
from tkinter.ttk import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from VisualizeClasses import *

root = Tk()
root.geometry('1200x900')

# user frame

User_Input_frame = t.Frame(root, background="snow")

Features_list = ["X1", "X2", "X3", "X4"]

Class_list = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
selected_class1 = StringVar()
selected_class2 = StringVar()
selected_feature1 = StringVar()
selected_feature2 = StringVar()
bias_selection = IntVar()
epochs_number = IntVar()
LR = DoubleVar()

Label(User_Input_frame, text="Class 1", background="snow").place(x=100, y=10)
class1_cb = Combobox(User_Input_frame, values=Class_list, textvariable=selected_class1)
class1_cb.place(x=200, y=10)

Label(User_Input_frame, text="Class 2", background="snow", width=7).place(x=100, y=40)
class2_cb = Combobox(User_Input_frame, textvariable=selected_class2)
class2_cb.place(x=200, y=40)

Label(User_Input_frame, text="Feature 1", background="snow").place(x=100, y=70)
feature1_cb = Combobox(User_Input_frame, values=Features_list, textvariable=selected_feature1)
feature1_cb.place(x=200, y=70)

Label(User_Input_frame, text="Feature 2", background="snow").place(x=100, y=100)
feature1_cb2 = Combobox(User_Input_frame, textvariable=selected_feature2)
feature1_cb2.place(x=200, y=100)

Label(User_Input_frame, text="Learning rate", width=15, background="snow").place(x=100, y=150)
t.ttk.Entry(User_Input_frame, width=10, textvariable=LR).place(x=200, y=150)

Label(User_Input_frame, text="epochs number", width=15, background="snow").place(x=100, y=180)
t.ttk.Entry(User_Input_frame, width=10, textvariable=epochs_number).place(x=200, y=180)

Checkbutton(User_Input_frame, text=' Add Bias ', variable=bias_selection, onvalue=1, offvalue=0).place(x=200, y=220)

TrainButton = Button(User_Input_frame, text="Train")
TrainButton.place(x=150, y=260)

SwitchButtonUser = Button(User_Input_frame, text="Go to Plotting One")
SwitchButtonUser.place(x=350, y=260)

Testlable = Label(User_Input_frame, text="", font='Helvetica 10 bold', background="snow")
Testlable.place(x=550, y=10)

TestFFlable = Label(User_Input_frame, text="", font='Helvetica 10 bold', background="snow")
TestFFlable.place(x=550, y=40)
TestFPlable = Label(User_Input_frame, text="", font='Helvetica 10 bold', background="snow")
TestFPlable.place(x=550, y=70)
TestPFlable = Label(User_Input_frame, text="", font='Helvetica 10 bold', background="snow")
TestPFlable.place(x=550, y=100)
TestPPlable = Label(User_Input_frame, text="", font='Helvetica 10 bold', background="snow")
TestPPlable.place(x=550, y=130)
TestAccLable = Label(User_Input_frame, text="", font='Helvetica 10 bold', background="snow")
TestAccLable.place(x=550, y=160)

Trainlable = Label(User_Input_frame, text="", font='Helvetica 10 bold', background="snow")
Trainlable.place(x=750, y=10)
TrainFFlable = Label(User_Input_frame, text="", font='Helvetica 10 bold', background="snow")
TrainFFlable.place(x=750, y=40)
TrainFPlable = Label(User_Input_frame, text="", font='Helvetica 10 bold', background="snow")
TrainFPlable.place(x=750, y=70)
TrainPFlable = Label(User_Input_frame, text="", font='Helvetica 10 bold', background="snow")
TrainPFlable.place(x=750, y=100)
TrainPPlable = Label(User_Input_frame, text="", font='Helvetica 10 bold', background="snow")
TrainPPlable.place(x=750, y=130)
TrainAccLable = Label(User_Input_frame, text="", font='Helvetica 10 bold', background="snow")
TrainAccLable.place(x=750, y=160)


WightsLable = Label(User_Input_frame, text="", font='Helvetica 10 bold', background="snow")
WightsLable.place(x=550, y=250)

# build plotting frame
Plotting_frame = t.Frame(root, background="snow")

FigureCanvasTkAgg(Plot_2_Classes(), Plotting_frame)._tkcanvas.pack(fill=BOTH, expand=1)

SwitchButtonPlotting = Button(Plotting_frame, text="Go to User Input")
SwitchButtonPlotting.place(x=550, y=60)
