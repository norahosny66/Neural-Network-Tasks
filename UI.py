
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from VisualizeClasses import *
from UI_Attributes import *
def SwitchFrame(frame1,frame2):
    frame1.pack_forget()
    frame2.pack(fill=BOTH,expand=1)

def Bind_Feature1(event):
    selected_feature2.set(" ")
    features_list2 = [x for x in Features_list if not x in [selected_feature1.get()]]
    features2_cb = Combobox(User_Input_frame, values=features_list2, textvariable=selected_feature2).place(x=200, y=100)
    features2_label.place(x=100,y=100)
def UserInputFrameBuilder ():

 feature1_cb.place(x=200,y=70)
 feature1_label.place(x=100,y=70)
 feature1_cb.bind('<<ComboboxSelected>>', Bind_Feature1)
 class1_cb.place(x=200, y=10)
 class1_cb.bind('<<ComboboxSelected>>', Bind_Class1)
 learning_rate.place(x=200,y=150)
 epochs.place(x=200, y=180)
 Bias_CheckBox .place(x=200,y=220)
 button1 = Button(User_Input_frame, text="Go to Plotting One",command=lambda:SwitchFrame(User_Input_frame,Plotting_frame))
 button1.place(x=350,y=260)

def return_user_input():
    return selected_feature1.get(), selected_feature2.get(), selected_class1.get(),selected_class2.get(),epochs_number.get(),LR.get(),bias_selection.get()

def Bind_Class1(event):
    selected_class2.set(" ")
    Class_list2 = [x for x in Class_list if not x in [selected_class1.get()]]
    class2_cb = Combobox(User_Input_frame, values=Class_list2, textvariable=selected_class2).place(x=200, y=40)
    class2_label = Label(User_Input_frame, text="Class 2",  width = 7)
    class2_label.place(x=100,y=40)

def UI_Controller():
    PlottingFrameBuilder()
    #build user input frame
    UserInputFrameBuilder()
    #set plotting frame as initial scene
    Plotting_frame.pack(fill=BOTH, expand=1)
    t.mainloop()
def PlottingFrameBuilder():
    # build plotting frame
    canvas = FigureCanvasTkAgg(Plot_2_Classes(), Plotting_frame)
    canvas._tkcanvas.pack(fill=BOTH, expand=1)
    button2 = Button(Plotting_frame, text="Go to User Input",
                     command=lambda: SwitchFrame(Plotting_frame, User_Input_frame))
    button2.place(x=550, y=60)