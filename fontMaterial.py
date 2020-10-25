from PyQt5 import QtGui

class FontMaterial():
    def __init__(self, size):
        self.size = size
        self.font = QtGui.QFont()
        self.font.setPointSize(self.size)

    def fontSize(self):
        return self.font
   
