# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from UI import *
from ReadDataset import *
from VisualizeClasses import *
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    read_data()  # Press Ctrl+F8 to toggle the breakpoint.
    feature1,feature2,class1,class2,LR,epochs=UserInput()
    Plot_2_Classes(Dict[feature1], Dict[feature2],class1,class2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
