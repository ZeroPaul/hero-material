from PyQt5 import QtCore, QtGui, QtWidgets

class QButton():
	def __init__(self, name_button=None, central=None, ud=None):
		self.name_button = name_button
		self.central = central
		self.ud = ud

		self.button_name = str(self.name_button.replace(' ', '_').lower()) + "_button"

		self.button_basic = QtWidgets.QPushButton(self.central)
		self.button_basic.setGeometry(QtCore.QRect(140, 150, 91, 36))
		font = QtGui.QFont()
		self.button_basic.setFont(font)
		self.button_basic.setStyleSheet("QPushButton {\n"
        "    border-radius: 4px;\n"
        "    background-color: #ff4081;\n"
        "    color: #ffffff;\n"
        "    font-size: 14px;\n"
        "    font-weight: 500;\n"
        "    font-family: Roboto,Helvetica Neue,sans-serif;\n"
        "}")
		self.button_basic.setObjectName(self.button_name)
		self.button_basic.setText(self.name_button)
		self.shadow = QtWidgets.QGraphicsDropShadowEffect(self.central)
		self.shadow.setBlurRadius(10)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QtGui.QColor('black'))
		self.button_basic.setGraphicsEffect(self.shadow)

		self.button_basic.pressed.connect(lambda: self.pressButton())
		self.button_basic.clicked.connect(lambda: self.clickButton())

	def pressButton(self):
		self.shadow.setBlurRadius(20)
		self.shadow.setYOffset(3)

	def clickButton(self):
		self.shadow.setBlurRadius(10)
		self.shadow.setYOffset(0)

	def buttonAdd(self):
		return self.button_basic