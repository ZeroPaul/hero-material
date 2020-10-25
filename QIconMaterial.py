from PyQt5 import QtGui

class QIconMaterial():
    def __init__(self, icon_file):
        self.icon_file = icon_file
        
        self.icon = QtGui.QIcon()
        self.pix = QtGui.QPixmap(self.icon_file)
        self.icon.addPixmap(self.pix, QtGui.QIcon.Normal, QtGui.QIcon.Off)

    def iconSVG(self):
        return self.icon
