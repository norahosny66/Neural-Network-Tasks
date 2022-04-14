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

Class_list = ['Sigmoid', 'Hyperbolic-Tangent-sigmoid ']




HiddenLayers =IntVar()
Neurons = StringVar()
LR = DoubleVar()
Epochs = IntVar()
selected_Activation_fn = StringVar()
bias_selection = IntVar()

Label(User_Input_frame, text="Hidden Layers", width=15, background="snow").place(x=100, y=10)
t.ttk.Entry(User_Input_frame, width=10, textvariable=HiddenLayers).place(x=220, y=10)

Label(User_Input_frame, text="#Neurons", width=15, background="snow").place(x=100, y=40)
t.ttk.Entry(User_Input_frame, width=10, textvariable=Neurons).place(x=220, y=40)

Label(User_Input_frame, text="Learning rate", width=15, background="snow").place(x=100, y=70)
t.ttk.Entry(User_Input_frame, width=10, textvariable=LR).place(x=220, y=70)

Label(User_Input_frame, text="Epochs", width=15, background="snow").place(x=100, y=100)
t.ttk.Entry(User_Input_frame, width=10, textvariable=Epochs).place(x=220, y=100)

Label(User_Input_frame, text="Activation Function", background="snow").place(x=100, y=130)
class1_cb = Combobox(User_Input_frame, values=Class_list, textvariable=selected_Activation_fn)#selected class1
class1_cb.place(x=220, y=130)



Checkbutton(User_Input_frame, text=' Add Bias ', variable=bias_selection, onvalue=1, offvalue=0).place(x=230, y=170)

TrainButton = Button(User_Input_frame, text="Train")
TrainButton.place(x=150, y=170)










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





