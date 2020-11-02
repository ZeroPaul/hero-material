from PyQt5 import QtGui

class FontMaterial():
    def __init__(self, size):
        self.size = size
        # self.weight = weight
        self.font = QtGui.QFont()
        self.font.setPointSize(self.size)
        # self.font.setWeight(self.weight)

    def fontSize(self):
        return self.font
   
