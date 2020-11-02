from PyQt5 import QtCore, QtGui, QtWidgets
from qiconmaterial import QIconMaterial

class QButtonIco():
	def __init__(self, name_ico=None, central=None, xh=0, yv=0):
		self.name_ico = name_ico
		self.central = central
		self.xh = xh
		self.yv = yv

		self.ico_name = str(self.name_ico.replace(' ', '_').lower()) + "_ico"

		self.ico_button = QtWidgets.QPushButton(self.central)
		self.ico_button.setGeometry(QtCore.QRect(self.xh, self.yv, 24, 24))
		self.ico_button.setMinimumSize(QtCore.QSize(24, 24))
		self.ico_button.setMaximumSize(QtCore.QSize(24, 24))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.ico_button.sizePolicy().hasHeightForWidth())
		self.ico_button.setSizePolicy(sizePolicy)
		# self.ico_button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
		# self.ico_button.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.ico_button.setStyleSheet("""
        	QPushButton {
		    	border-radius: 12px;
		    	background: none;
		    	border:0px; outline:0;
		    	text-align: center;
			}
			QPushButton:hover {
		    	background: #c5c5c5;
			}
		""")
		self.ico_button.setText("")
		self.iconn = QIconMaterial("favorite-24px.svg").iconSVG()
		self.ico_button.setIcon(self.iconn)
		self.ico_button.setIconSize(QtCore.QSize(16, 16))
		self.ico_button.setAutoRepeatDelay(300)
		self.ico_button.setAutoRepeatInterval(300)
		self.ico_button.setObjectName(self.ico_name)

	def iconGrid(self):
		return self.ico_button
		

