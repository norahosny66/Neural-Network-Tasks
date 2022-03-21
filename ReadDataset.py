
X1 = []
X2 = []
X3 = []
X4 = []
class_ = []
Dict=dict({"X1": X1, "X2": X2, "X3": X3, "X4": X4})
def read_data():
    with open('IrisData.txt') as f:
      line=f.readline()
      while (line):
        line = f.readline().split(",")
        if len(line)<5:
            break
        X1.append(float(line[0]))
        X2.append(float(line[1]))
        X3.append(float(line[2]))
        X4.append(float(line[3]))
        class_.append(line[4])
