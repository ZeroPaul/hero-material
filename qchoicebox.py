from PyQt5 import QtCore, QtWidgets

class QChoiceBox(QtWidgets.QComboBox):
    focus_in_signal = QtCore.pyqtSignal()
    focus_out_signal = QtCore.pyqtSignal()
    popupAboutToBeShown = QtCore.pyqtSignal()

    def focusInEvent(self, event):
        self.focus_in_signal.emit()
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.focus_out_signal.emit()
    
    def showPopup(self):
        super(QChoiceBox, self).showPopup()
        self.popupAboutToBeShown.emit()