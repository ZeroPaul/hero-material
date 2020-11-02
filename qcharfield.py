from PyQt5 import QtCore, QtGui, QtWidgets
from qinputedit import QInputEdit
from fontMaterial import FontMaterial
from qiconmaterial import QIconMaterial

class QCharField():
    def __init__(self, name_field=None, size_font=11, max_length=66, central=None, ud=None):

        self.name_field = name_field
        self.size_font = size_font
        self.max_length = max_length
        self.central = central
        self.ud = ud

        self.label_name = str(self.name_field.replace(' ', '_').lower()) + "_label"
        self.input_name = str(self.name_field.replace(' ', '_').lower()) + "_input"
        self.validation_name = str(self.name_field.replace(' ', '_').lower()) + "_validation"
        self.button_name = str(self.name_field.replace(' ', '_').lower()) + "_button"

        self.font_standart = FontMaterial(self.size_font).fontSize()
        self.font_minus = FontMaterial(self.size_font - 3).fontSize()

        self.label = QtWidgets.QLabel(self.central)
        self.label.setGeometry(QtCore.QRect(80, self.ud, 181, 31))
        self.label.setFont(self.font_standart)
        self.label.setStyleSheet("color: #1E88E5;")
        self.label.setObjectName(self.label_name)
        self.label.setText(self.name_field)

        self.label_validation = QtWidgets.QLabel(self.central)
        self.label_validation.setGeometry(QtCore.QRect(80, self.ud + 20, 181, 31))
        self.label_validation.setFont(self.font_minus)
        self.label_validation.setStyleSheet("color: #e53935;")
        self.label_validation.setObjectName(self.validation_name)
        self.label_validation.setText("error_message")



        self.input_material = QInputEdit(self.central)
        self.input_material.setGeometry(QtCore.QRect(80, self.ud, 181, 31))
        self.input_material.setFont(self.font_standart)
        self.input_material.setStyleSheet("""
            QLineEdit { background: transparent;
                border: none;
                border-bottom:1px solid #1E88E5;
            }
            QLineEdit:focus {
                border-bottom:2px solid #0D47A1;
            }
        """)
        self.input_material.setMaxLength(self.max_length)
        self.input_material.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_material.setObjectName(self.input_name)
        self.input_material.focus_in_signal.connect(lambda: self.focus_in())
        self.input_material.focus_out_signal.connect(lambda: self.focus_out())
        self.input_material.cursorPositionChanged.connect(lambda: self.showClear())

        self.button_pass = QtWidgets.QPushButton(self.central)
        self.button_pass.setGeometry(QtCore.QRect(240, self.ud + 4, 24, 24))
        self.button_pass.setStyleSheet("QPushButton  {\n"
        "    border-radius: 12; border: 0; outline:0;\n"
        "    background: transparent;\n"
        "    color: #ff00ff;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: #c5c5c5;\n"
        "}")
        self.button_pass.setText("")
        self.button_pass.hide()

        self.icon_clear = QIconMaterial("close-24px.svg").iconSVG()
        self.button_pass.setIcon(self.icon_clear)
        self.button_pass.setToolTip("Clear")
        self.button_pass.setObjectName(self.button_name)
        self.status = 0
        self.button_pass.clicked.connect(lambda: self.clearChar())

    def focus_in(self):
        self.label.setGeometry(QtCore.QRect(80, self.ud - 20, 181, 31))
        self.label.setStyleSheet("""
            color: #0D47A1;
        """)
        self.label.setFont(self.font_minus)
        
    def focus_out(self):
        self.label.setStyleSheet("""
            color: #1E88E5;
        """)
        if self.input_material.text() == "":
            self.label.setGeometry(QtCore.QRect(80, self.ud, 181, 31))
            self.label.setFont(self.font_standart)

    def showClear(self):
        if self.input_material.text() == "":
            self.button_pass.hide()
        else:
            self.button_pass.show()

    def clearChar(self):
        self.input_material.setText("")
        self.input_material.setFocus(True)
        self.button_pass.hide()

class QPasswordField():

    def __init__(self, name_field=None, size_font=11, max_length=66, central=None, ud=None):
        self.name_field = name_field
        self.size_font = size_font
        self.max_length = max_length
        self.central = central
        self.ud = ud

        self.label_name = str(self.name_field.replace(' ', '_').lower()) + "_label"
        self.input_name = str(self.name_field.replace(' ', '_').lower()) + "_input"
        self.validation_name = str(self.name_field.replace(' ', '_').lower()) + "_validation"
        self.button_name = str(self.name_field.replace(' ', '_').lower()) + "_button"

        self.font_standart = FontMaterial(self.size_font).fontSize()
        self.font_minus = FontMaterial(self.size_font - 3).fontSize()

        self.label = QtWidgets.QLabel(self.central)
        self.label.setGeometry(QtCore.QRect(80, self.ud, 181, 31))
        self.label.setFont(self.font_standart)
        self.label.setStyleSheet("color: #1E88E5;")
        self.label.setObjectName(self.label_name)
        self.label.setText(self.name_field)

        self.label_validation = QtWidgets.QLabel(self.central)
        self.label_validation.setGeometry(QtCore.QRect(80, self.ud + 20, 181, 31))
        self.label_validation.setFont(self.font_minus)
        self.label_validation.setStyleSheet("color: #e53935;")
        self.label_validation.setObjectName(self.validation_name)
        self.label_validation.setText("error_message")

        self.input_material = QInputEdit(self.central)
        self.input_material.setGeometry(QtCore.QRect(80, self.ud, 181, 31))
        self.input_material.setFont(self.font_standart)
        self.input_material.setStyleSheet("""
            QLineEdit { background: transparent;
                border: none;
                border-bottom:1px solid #1E88E5;
            }
            QLineEdit:focus {
                border-bottom:2px solid #0D47A1;
            }
        """)
        self.input_material.setMaxLength(self.max_length)
        self.input_material.setEchoMode(QInputEdit.Password)
        self.input_material.setObjectName(self.input_name)
        self.input_material.focus_in_signal.connect(lambda: self.focus_in())
        self.input_material.focus_out_signal.connect(lambda: self.focus_out())

        self.button_pass = QtWidgets.QPushButton(self.central)
        self.button_pass.setGeometry(QtCore.QRect(240, self.ud + 4, 24, 24))
        self.button_pass.setStyleSheet("QPushButton  {\n"
        "    border-radius: 12;\n"
        "    background: transparent;\n"
        "    color: #ff00ff;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: #c5c5c5;\n"
        "}")
        self.button_pass.setText("")

        self.icon_eye = QIconMaterial("visibility-24px.svg").iconSVG()
        self.icon_no_eye = QIconMaterial("visibility_off-24px.svg").iconSVG()

        self.button_pass.setIcon(self.icon_eye)
        self.button_pass.setToolTip("Show Password")
        self.button_pass.setObjectName(self.button_name)
        self.status = 0
        self.button_pass.clicked.connect(lambda: self.showPassword())

    def focus_in(self):
        self.label.setGeometry(QtCore.QRect(80, self.ud - 20, 181, 31))
        self.label.setStyleSheet("""
            color: #0D47A1;
        """)
        self.label.setFont(self.font_minus)

    def focus_out(self):
        self.label.setStyleSheet("""
            color: #1E88E5;

        """)
        if self.input_material.text() == "":
            self.label.setGeometry(QtCore.QRect(80, self.ud, 181, 31))
            self.label.setFont(self.font_standart)



    def showPassword(self):
        if self.status == 1:
            self.status = 0
            self.input_material.setEchoMode(QInputEdit.Password)
            self.button_pass.setIcon(self.icon_eye)
            self.button_pass.setToolTip("Show Password")
            self.input_material.setFocus(True)
            self.input_material.setCursorPosition(len(self.input_material.text()));
        elif self.status == 0:
            self.status = 1
            self.input_material.setEchoMode(QInputEdit.Normal)
            self.button_pass.setIcon(self.icon_no_eye)
            self.button_pass.setToolTip("Hidde Password")
            self.input_material.setFocus(True)
            self.input_material.setCursorPosition(len(self.input_material.text()));
