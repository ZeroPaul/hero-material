from PyQt5 import QtCore, QtGui, QtWidgets
from qcharfield import QCharField, QPasswordField
from qchoicefield import QChoiceField
from qfabbutton import QFabButton, QFabMiniButton
from qiconmaterial import QIconMaterial
from qbutton import QButton
from qcalendar import QCalendar, QButtonYear
from qbuttonico import QButtonIco
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # username = QCharField(name_field="nombre de", size_font=11, max_length=10, central=self.centralwidget, ud=80)
        # password = QPasswordField(name_field="Password", size_font=11, max_length=200, central=self.centralwidget, ud=140)
        # choice = QChoiceField(name_field="City", size_font=11, central=self.centralwidget, ud=80)
        # fabmini = QFabMiniButton(name_field="fabmini", central=self.centralwidget, ud=190)
        # fab = QFabButton(name_field="fab", central=self.centralwidget, ud=190)
        # basic_button = QButton(name_button="Hero", central=self.centralwidget, ud=None)
        # ico_button = QButtonIco(name_ico="eye", central=self.centralwidget, xh=80, yv=70)
        calendar_all = QCalendar(name_calendar="callen", central=self.centralwidget)

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