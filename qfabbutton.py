from PyQt5 import QtCore, QtGui, QtWidgets
from qiconmaterial import QIconMaterial

class QFabButton():
	def __init__(self, name_field=None, central=None, ud=None):
		self.name_field = name_field
		self.central = central
		self.ud = ud

		self.button_name = str(self.name_field.replace(' ', '_').lower()) + "_button"

		self.fabButton = QtWidgets.QPushButton(self.central)
		self.fabButton.setEnabled(True)
		self.fabButton.setGeometry(QtCore.QRect(140, 280, 56, 56))
		
		self.fabButton.setStyleSheet("QPushButton {\n"
        "background: #FF8A80; border-radius: 28; border: 0; outline:0;\n"
        "}")
		self.fabButton.setText("")
		self.icon_eye = QIconMaterial("visibility-24px.svg").iconSVG()
		self.fabButton.setIcon(self.icon_eye)
		self.fabButton.setIconSize(QtCore.QSize(24, 24))
		self.fabButton.setObjectName(self.button_name)
		self.shadow = QtWidgets.QGraphicsDropShadowEffect(self.central)
		self.shadow.setBlurRadius(20)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QtGui.QColor('black'))
		self.fabButton.setGraphicsEffect(self.shadow)

		self.fabButton.pressed.connect(lambda: self.pressButton())
		self.fabButton.clicked.connect(lambda: self.clickButton())

	def pressButton(self):
		self.shadow.setBlurRadius(50)

	def clickButton(self):
		self.shadow.setBlurRadius(20)

class QFabMiniButton():
	def __init__(self, name_field=None, central=None, ud=None):
		self.name_field = name_field
		self.central = central
		self.ud = ud

		self.button_name = str(self.name_field.replace(' ', '_').lower()) + "_button"

		self.fabButton = QtWidgets.QPushButton(self.central)
		self.fabButton.setEnabled(True)
		self.fabButton.setGeometry(QtCore.QRect(210, 290, 40, 40))
		self.fabButton.setStyleSheet("QPushButton {\n"
        "background: #FF8A80; border-radius: 20; border: 0; outline:0;\n"
        "}")
		self.fabButton.setText("")
		self.icon_eye = QIconMaterial("close-24px.svg").iconSVG()
		self.fabButton.setIcon(self.icon_eye)
		self.fabButton.setIconSize(QtCore.QSize(24, 24))
		self.fabButton.setObjectName(self.button_name)
		self.shadow = QtWidgets.QGraphicsDropShadowEffect(self.central)
		self.shadow.setBlurRadius(15)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QtGui.QColor('black'))
		self.fabButton.setGraphicsEffect(self.shadow)

		self.fabButton.pressed.connect(lambda: self.pressButton())
		self.fabButton.clicked.connect(lambda: self.clickButton())

	def pressButton(self):
		self.shadow.setBlurRadius(35)

	def clickButton(self):
		self.shadow.setBlurRadius(15)
