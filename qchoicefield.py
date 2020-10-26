from PyQt5 import QtCore, QtWidgets
from fontMaterial import FontMaterial
from qchoicebox import QChoiceBox
from qiconmaterial import QIconMaterial

class QChoiceField():
	def __init__(self, name_field=None, size_font=11, central=None, ud=None):
		self.name_field = name_field
		self.size_font = size_font
		self.central = central
		self.ud = ud

		self.label_name = str(self.name_field.replace(' ', '_').lower()) + "_label"
		self.combo_name = str(self.name_field.replace(' ', '_').lower()) + "_combo"
		# self.validation_name = str(self.name_field.replace(' ', '_').lower()) + "_validation"
		self.button_name = str(self.name_field.replace(' ', '_').lower()) + "_button"

		self.label_font = FontMaterial(self.size_font - 3).fontSize()

		self.label = QtWidgets.QLabel(self.central)
		self.label.setGeometry(QtCore.QRect(68, 151 - 20, 201, 31))
		self.label.setFont(self.label_font)
		self.label.setStyleSheet("color: #1E88E5;")
		self.label.setObjectName(self.label_name)
		self.label.setText(self.name_field)

		self.comboBox = QChoiceBox(self.central)
		self.comboBox.setGeometry(QtCore.QRect(68, 151, 201, 31))
		self.comboBox.setAutoFillBackground(False)
		self.comboBox.setStyleSheet("""QComboBox{
            background: transparent;
            border: 0px;
            border-bottom:1px solid #1E88E5;
        }
        QComboBox:focus{
            border-bottom:2px solid #0D47A1;
        }
        QComboBox QAbstractItemView {
            background: #ffffff;
            selection-background-color: #e8e8e8;
            outline: none;
        }
        QComboBox::drop-down
        {
            border-width: 0px;
        }
        QWidget::item {
            color: #1E88E5;
            padding: 9px 11px;
        }
        QWidget::item:hover {
            background: #c5c5c5;
            color: #1E88E5;
            padding: 9px 11px;
        }
        QWidget::item:selected:active{
            background: #c5c5c5;
            color: #1E88E5;
            padding: 9px 11px;
        }
        QComboBox QAbstractScrollArea QScrollBar:vertical {
            border: none;
            background-color: #ffffff;
            margin: 0px 0 0px 0;
            width: 8px;
        }
        QComboBox QAbstractScrollArea QScrollBar::handle:vertical {
            background: black;
            min-height: 50px;
            border-radius: 4px;
        }
        QComboBox QAbstractScrollArea QScrollBar::up-arrow:vertical, QComboBox QAbstractScrollArea QScrollBar::down-arrow:vertical {
            border: none;
            background: none;
            color: none;
        }
        QComboBox QAbstractScrollArea QScrollBar::add-line:vertical {
            border: none;
            background: none;
            width: 0px;
            height: 0px;
        }
        QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {
            border: none;
            background: none;
            width: 0px;
            height: 0px;
        }
        """)
		self.comboBox.setEditable(False)
		self.comboBox.setMaxVisibleItems(4)
		self.comboBox.setObjectName(self.combo_name)
		self.comboBox.addItem("1")
		self.comboBox.addItem("2")
		self.comboBox.addItem("3")
		self.comboBox.addItem("4")
		self.comboBox.addItem("5")
		self.comboBox.addItem("6")
		self.comboBox.addItem("7")
		self.comboBox.addItem("8")
		self.comboBox.addItem("9")
		self.comboBox.addItem("10")
		delegate = QtWidgets.QStyledItemDelegate(self.comboBox)
		self.comboBox.setItemDelegate(delegate)
		self.comboBox.currentIndexChanged.connect(lambda: self.selectionChange())
		self.comboBox.focus_in_signal.connect(lambda: self.focus_in())
		self.comboBox.focus_out_signal.connect(lambda: self.focus_out())
		self.comboBox.activated.connect(lambda: self.activatedSelection())

		self.button_popup = QtWidgets.QPushButton(self.central)
		self.button_popup.setGeometry(QtCore.QRect(240, 154, 24, 24))
		self.button_popup.setStyleSheet("""
        	QPushButton {
        		border-radius: 12; border: 0; outline: 0;
        		background: transparent;
        		color: #ff00ff;
        	}
			QPushButton:hover {
				background: #c5c5c5;

        	}
        	""")
		self.button_popup.setText("")
		self.icon_arrow = QIconMaterial("expand_more-24px.svg").iconSVG()
		self.button_popup.setIcon(self.icon_arrow)
		self.button_popup.setToolTip("Show Options")
		self.button_popup.setObjectName(self.button_name)
		self.button_popup.clicked.connect(lambda: self.buttonPopup())

	def buttonPopup(self):
		self.comboBox.showPopup()

	def focus_in(self):
		self.label.setStyleSheet("color: #0D47A1;")

	def focus_out(self):
		self.label.setStyleSheet("color: #1E88E5;")

	def activatedSelection(self):
		self.label.setStyleSheet("color: #0D47A1;")

	def selectionChange(self):
		self.comboBox.setFocus(True)