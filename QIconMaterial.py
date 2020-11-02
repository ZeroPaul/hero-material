from PyQt5 import QtGui, QtCore

class QIconMaterial():
    def __init__(self, icon_file):
        self.icon_file = icon_file
        self.icon = QtGui.QIcon()
        self.pix = QtGui.QPixmap(self.icon_file)

        # self.mask = self.pix.createMaskFromColor(QtGui.QColor('black'), QtCore.Qt.MaskOutColor)
        # self.pix.fill(QtGui.QColor("red"));
        # self.pix.setMask(self.mask)

        self.icon.addPixmap(self.pix, QtGui.QIcon.Normal, QtGui.QIcon.Off)

    def iconSVG(self):
        return self.icon
