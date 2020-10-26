from PyQt5 import QtCore, QtGui, QtWidgets
from qcharfield import QCharField, QPasswordField
from qchoicefield import QChoiceField
from qiconmaterial import QIconMaterial
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        username = QCharField(name_field="Username", size_font=11, max_length=200, central=self.centralwidget, ud=80)
        password = QPasswordField(name_field="Password", size_font=11, max_length=200, central=self.centralwidget, ud=140)
        # choice = QChoiceField(name_field="City", size_font=11, central=self.centralwidget, ud=80)        

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())