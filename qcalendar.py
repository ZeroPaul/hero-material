import calendar
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets
from fontMaterial import FontMaterial
from qbutton import QButton
from qbuttonico import QButtonIco

class QCalendarBuilder():
	def __init__(self):
		self.today_now = self.calendarToday()

	def calendarToday(self):
		today = date.today()
		c_day = int(today.strftime("%d"))
		c_month = int(today.strftime("%m"))
		c_year = int(today.strftime("%Y"))
		return [c_day, c_month, c_year]

	def calendarNumberToday(self):
		day_number = calendar.weekday(
			self.today_now[2], self.today_now[1], self.today_now[0]
		)
		day_name = calendar.day_name[day_number]
		day_index = self.calendarDay().index(day_name)
		return [day_name, day_index]

	def calendarNumberDay(self, syear, smonth, sday):
		day_number = calendar.weekday(syear, smonth, sday)
		day_name = calendar.day_name[day_number]
		day_index = self.calendarDay().index(day_name)
		return [day_name, day_index]

	def calendarMonthrange(self, syear, smonth):
		start_month = 1
		end_month = calendar.monthrange(syear, smonth)[1]
		return [start_month, end_month]

	def calendarDay(self):
		list_day = list(calendar.day_name)
		list_day = list_day[-1:] + list_day[:-1]
		return list_day

	def calendarMonth(self, index):
		list_month = list(calendar.month_name)
		# list_month.pop(0)
		return list_month[index]

class QCalendar(QCalendarBuilder):
	def __init__(self, name_calendar=None, central=None):
		self.name_calendar = name_calendar
		self.central = central
		QCalendarBuilder.__init__(self)

		self.background_name = str(self.name_calendar.replace(' ', '_').lower()) + "_back"
		self.topbutton_name = str(self.name_calendar.replace(' ', '_').lower()) + "_top"

		# background
		self.verticalFrame = QtWidgets.QFrame(self.central)
		self.verticalFrame.setGeometry(QtCore.QRect(10, 150, 244, 280))
		self.verticalFrame.setMinimumSize(QtCore.QSize(244, 280))
		self.verticalFrame.setMaximumSize(QtCore.QSize(244, 280))
		self.verticalFrame.setStyleSheet("""
        	QFrame {
        		background: #dfdfdf;
				border-radius: 5px;
			}
		""")
		self.verticalFrame.setObjectName(self.background_name)

		# Other box
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("topbutton_name")

		# buttons top
		self.horizontalFrame = QtWidgets.QFrame(self.verticalFrame)
		self.horizontalFrame.setMinimumSize(QtCore.QSize(244, 40))
		self.horizontalFrame.setMaximumSize(QtCore.QSize(244, 40))
		self.horizontalFrame.setObjectName("horizontalFrame_2")

		self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 10)
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setObjectName("horizontalLayout_2")

		self.button_month = QButton(name_button="Hero", central=self.horizontalFrame, ud=None)
		self.button_month.buttonAdd().setMinimumSize(QtCore.QSize(166, 30))
		self.button_month.buttonAdd().setMaximumSize(QtCore.QSize(166, 30))
		self.button_month.buttonAdd().clicked.connect(lambda: self.changeYear())

		self.horizontalLayout.addWidget(self.button_month.buttonAdd())

		self.status_lef = "day"
		self.status_right = "day"

		self.left_button = QButtonIco(name_ico="eyed", central=self.horizontalFrame, xh=0, yv=0)
		self.left_button.iconGrid().clicked.connect(lambda: self.allLef())
		self.horizontalLayout.addWidget(self.left_button.iconGrid())

		self.right_button = QButtonIco(name_ico="eyes", central=self.horizontalFrame, xh=0, yv=0)
		self.right_button.iconGrid().clicked.connect(lambda: self.allRight())
		self.horizontalLayout.addWidget(self.right_button.iconGrid())

		self.verticalLayout.addWidget(self.horizontalFrame)
		self.reset_day = []
		self.reset_year = ""
		self.year_select = ""
		self.month_select = ""
		self.status_button = False
		self.frameDay()

	def frameDay(self):
		#name days box
		self.verticalFrameDay = QtWidgets.QFrame(self.verticalFrame)
		self.verticalFrameDay.setMinimumSize(QtCore.QSize(244, 215))
		self.verticalFrameDay.setMaximumSize(QtCore.QSize(244, 215))
		self.verticalFrameDay.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.verticalFrameDay.setObjectName("verticalFrameDay")
		
		self.verticalLayoutDay = QtWidgets.QVBoxLayout(self.verticalFrameDay)
		self.verticalLayoutDay.setContentsMargins(0, 0, 0, 0)
		self.verticalLayoutDay.setSpacing(0)
		self.verticalLayoutDay.setObjectName("verticalLayoutDay")

		self.gridFrame = QtWidgets.QFrame(self.verticalFrame)
		self.gridFrame.setMinimumSize(QtCore.QSize(244, 30))
		self.gridFrame.setMaximumSize(QtCore.QSize(244, 30))
		self.gridFrame.setObjectName("gridFrame")

		self.gridLayoutDay = QtWidgets.QGridLayout(self.gridFrame)
		self.gridLayoutDay.setObjectName("gridLayoutDay")
		self.day_1 = QLabelDate(name_label="S", size_font=10, central=self.gridFrame)
		self.gridLayoutDay.addWidget(self.day_1.labelGrid(), 0, 6, 1, 1)
		self.day_2 = QLabelDate(name_label="M", size_font=10, central=self.gridFrame)
		self.gridLayoutDay.addWidget(self.day_2.labelGrid(), 0, 7, 1, 1)
		self.day_3 = QLabelDate(name_label="T", size_font=10, central=self.gridFrame)
		self.gridLayoutDay.addWidget(self.day_3.labelGrid(), 0, 8, 1, 1)
		self.day_4 = QLabelDate(name_label="W", size_font=10, central=self.gridFrame)
		self.gridLayoutDay.addWidget(self.day_4.labelGrid(), 0, 9, 1, 1)
		self.day_5 = QLabelDate(name_label="T", size_font=10, central=self.gridFrame)
		self.gridLayoutDay.addWidget(self.day_5.labelGrid(), 0, 10, 1, 1)
		self.day_6 = QLabelDate(name_label="F", size_font=10, central=self.gridFrame)
		self.gridLayoutDay.addWidget(self.day_6.labelGrid(), 0, 11, 1, 1)
		self.day_7 = QLabelDate(name_label="S", size_font=10, central=self.gridFrame)
		self.gridLayoutDay.addWidget(self.day_7.labelGrid(), 0, 12, 1, 1)

		self.verticalLayoutDay.addWidget(self.gridFrame)

		#divider
		self.line_divider = QtWidgets.QFrame(self.verticalFrameDay)
		self.line_divider.setMinimumSize(QtCore.QSize(244, 1))
		self.line_divider.setMaximumSize(QtCore.QSize(244, 1))
		self.line_divider.setStyleSheet("border: 1px solid #a1a1a1;")
		self.line_divider.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_divider.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_divider.setObjectName("line_divider")
		self.verticalLayoutDay.addWidget(self.line_divider)

		self.verticalLayout.addWidget(self.verticalFrameDay)

		self.grid_FrameNumers = QtWidgets.QFrame(self.verticalFrameDay)
		self.grid_FrameNumers.setMinimumSize(QtCore.QSize(244, 190))
		self.grid_FrameNumers.setMaximumSize(QtCore.QSize(244, 190))
		self.grid_FrameNumers.setObjectName("grid_FrameNumers")

		self.gridLayoutNumers = QtWidgets.QGridLayout(self.grid_FrameNumers)
		self.gridLayoutNumers.setObjectName("gridLayoutNumers")

		self.buttons_all = {}
		if self.reset_day:
			self.date_now = self.reset_day
		else:
			self.date_now = self.today_now

		self.calendarNumbers(self.date_now)
		self.verticalLayoutDay.addWidget(self.grid_FrameNumers)
		self.status_lef = "day"
		self.status_right = "day"
		print("load days")

	def frameMonth(self, fyear):
		self.verticalFrameMonth = QtWidgets.QFrame(self.verticalFrame)
		self.verticalFrameMonth.setMinimumSize(QtCore.QSize(244, 215))
		self.verticalFrameMonth.setMaximumSize(QtCore.QSize(244, 215))
		self.verticalFrameMonth.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.verticalFrameMonth.setObjectName("verticalFrameMonth")

		self.verticalLayoutMonth = QtWidgets.QVBoxLayout(self.verticalFrameMonth)
		self.verticalLayoutMonth.setContentsMargins(0, 0, 0, 50)
		self.verticalLayoutMonth.setSpacing(0)
		self.verticalLayoutMonth.setObjectName("verticalLayoutMonth")

		self.line_divider = QtWidgets.QFrame(self.verticalFrameMonth)
		self.line_divider.setMinimumSize(QtCore.QSize(244, 1))
		self.line_divider.setMaximumSize(QtCore.QSize(244, 1))
		self.line_divider.setStyleSheet("border: 1px solid #a1a1a1;")
		self.line_divider.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_divider.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_divider.setObjectName("line_divider")
		self.verticalLayoutMonth.addWidget(self.line_divider)

		self.gridFrameMonth = QtWidgets.QFrame(self.verticalFrameMonth)
		self.gridFrameMonth.setMinimumSize(QtCore.QSize(244, 210))
		self.gridFrameMonth.setMaximumSize(QtCore.QSize(244, 210))
		self.gridFrameMonth.setObjectName("gridFrameMonth")
		
		self.gridLayoutMonth = QtWidgets.QGridLayout(self.gridFrameMonth)
		self.gridLayoutMonth.setContentsMargins(3, 3, 6, 0)
		self.gridLayoutMonth.setSpacing(6)
		self.gridLayoutMonth.setObjectName("gridLayoutMonth")

		self.buttons_mounths = {}

		month_old = False
		if self.month_select:
			month_old = True
		else:
			month_old = False

		a = 2
		y = -1
		x = 0
		c = 0
		for i in range(12):
			if c == a:
				a += 2
				y = 0
				x += 1
			else:
				y += 1
			c += 1
			g = self.calendarMonth(c)
			self.b_month = self.push = QButtonMonth(name_month=g, size_font=10, central=self.gridFrameMonth)
			self.b_month.buttonAdd().setCheckable(True)

			if month_old == True and self.month_select == c:
				self.b_month.buttonAdd().setChecked(True)

			self.b_month.buttonAdd().clicked.connect(lambda ch, g=g, f=fyear, c=c: self.monthSelect(g, f, c))
			self.gridLayoutMonth.addWidget(self.b_month.buttonAdd(), x, y, 1, 1)
			self.buttons_mounths[g] = self.b_month

		self.verticalLayoutMonth.addWidget(self.gridFrameMonth)
		self.verticalLayout.addWidget(self.verticalFrameMonth)
		self.button_month.buttonAdd().setText(str(fyear))
		self.status_lef = "month"
		self.status_right = "month"
		print("load month")

	def frameYear(self, fyear):
		self.verticalFrameYear = QtWidgets.QFrame(self.verticalFrame)
		self.verticalFrameYear.setMinimumSize(QtCore.QSize(244, 215))
		self.verticalFrameYear.setMaximumSize(QtCore.QSize(244, 215))
		self.verticalFrameYear.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.verticalFrameYear.setObjectName("verticalFrameYear")

		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrameYear)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 50)
		self.verticalLayout_2.setSpacing(0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")

		self.line_divider = QtWidgets.QFrame(self.verticalFrameYear)
		self.line_divider.setMinimumSize(QtCore.QSize(244, 1))
		self.line_divider.setMaximumSize(QtCore.QSize(244, 1))
		self.line_divider.setStyleSheet("border: 1px solid #a1a1a1;")
		self.line_divider.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_divider.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_divider.setObjectName("line_divider")
		self.verticalLayout_2.addWidget(self.line_divider)
		
		self.gridFramebutton = QtWidgets.QFrame(self.verticalFrameYear)
		self.gridFramebutton.setMinimumSize(QtCore.QSize(244, 210))
		self.gridFramebutton.setMaximumSize(QtCore.QSize(244, 210))
		self.gridFramebutton.setObjectName("gridFramebutton")
		
		self.gridLayout_3 = QtWidgets.QGridLayout(self.gridFramebutton)
		self.gridLayout_3.setContentsMargins(3, 3, 6, 0)
		self.gridLayout_3.setSpacing(6)
		self.gridLayout_3.setObjectName("gridLayout_3")

		self.buttons_years = {}

		if self.today_now[2] == fyear:
			fyear = fyear - 5
		else:
			fyear = fyear

		self.calendarYears(fyear)

		self.verticalLayout_2.addWidget(self.gridFramebutton)
		self.verticalLayout.addWidget(self.verticalFrameYear)
		self.status_lef = "year"
		self.status_right = "year"
		# print("load years")

	def calendarNumbers(self, tnow):
		t_day = tnow[0]
		t_month = tnow[1]
		t_year = tnow[2]
		name_month = self.calendarMonth(t_month)
		self.button_month.buttonAdd().setText(str(name_month) + " " + str(t_year))
		firts_day = self.calendarNumberDay(t_year, t_month, 1)[1]
		number_day = 0
		limit_day = self.calendarMonthrange(t_year, t_month)[1]
		r = 0
		a = 7
		c = 0
		o = 1
		x = -1
		for i in range(42):
			if i >= firts_day and number_day < limit_day:
				number_day += 1
				r = number_day
			else:
				r = ""
			
			if c == a:
				a += 7
				o += 1
				x = 0
			else:
				x += 1
			c += 1
			if r != "":
				self.push1 = QButtonDate(name_date= str(r), size_font=10, central=self.grid_FrameNumers, ud=12)
				if self.calendarToday()[0] == number_day and self.calendarToday()[1] == t_month and self.calendarToday()[2] == t_year:
					self.push1.buttonGrid().setStyleSheet("""
						QPushButton {
				    		border-radius: 14px;
			    			background: none;
			    			border: 2px solid #3f51b5;
						}
						QPushButton:hover {
			    			background: #bebebe;
						}
						QPushButton:checked {
							background: #3f51b5;
			    			color: #ffffff;
						}
						""")
				self.push1.buttonGrid().setCheckable(True)
				d = "{0}/{1}/{2}".format(r, t_month, t_year)
				self.push1.buttonGrid().clicked.connect(lambda ch, r=r: self.dateSelect(r))
				self.push1.buttonGrid().clicked.connect(lambda ch, d=d: self.setDate(d))
				self.gridLayoutNumers.addWidget(self.push1.buttonGrid(), o, x, 1, 1)
				self.buttons_all[r] = [self.push1, o, x]
				# print(o, x)

	def calendarYears(self, fyear):

		year_old = False
		if self.year_select:
			year_old = True
		else:
			year_old = False

		if self.reset_year:
			fyear = self.reset_year
		else:
			fyear = fyear

		self.year_now = fyear

		a = 4
		y = -1
		x = 0
		c = 0

		year_init = self.year_now
		init_year = self.year_now

		year_end = year_init + 20

		for i in range(20):
			if c == a:
				a += 4
				y = 0
				x += 1
			else:
				y += 1
			c += 1
			init_year += 1
			self.push = QButtonYear(name_year=str(init_year), size_font=10, central=self.gridFramebutton)
			if self.today_now[2] == init_year:
					self.push.buttonAdd().setStyleSheet("""
						QPushButton {
				    		border-radius: 14px;
			    			background: none;
			    			border: 2px solid #3f51b5;
						}
						QPushButton:hover {
			    			background: #bebebe;
						}
						QPushButton:checked {
							background: #3f51b5;
			    			color: #ffffff;
						}
						""")
			if year_old == True and self.year_select == init_year:
				self.push.buttonAdd().setChecked(True)

			self.push.buttonAdd().setCheckable(True)
			self.push.buttonAdd().clicked.connect(lambda ch, i=init_year: self.yearSelect(i))
			self.gridLayout_3.addWidget(self.push.buttonAdd(), x, y, 1, 1)
			self.buttons_years[init_year] = self.push
		self.button_month.buttonAdd().setText(str(year_init + 1) + " - " + str(year_end))


	def dateSelect(self, i):
		for key, value in self.buttons_all.items():
			if key == i:
				value[0].buttonGrid().setChecked(True)
			else:
				value[0].buttonGrid().setChecked(False)

	def monthSelect(self, i, f, c):
		for key, value in self.buttons_mounths.items():
			if key == i:
				value.buttonAdd().setChecked(True)
			else:
				value.buttonAdd().setChecked(False)
		
		self.verticalFrameMonth.deleteLater()
		self.reset_day = [1, c, f]
		self.frameDay()
		self.status_button = False
		self.year_select = f
		self.month_select = c

	def yearSelect(self, i):
		for key, value in self.buttons_years.items():
			if key == i:
				value.buttonAdd().setChecked(True)
			else:
				value.buttonAdd().setChecked(False)
		self.verticalFrameYear.deleteLater()
		self.frameMonth(i)

	def empty(self):
		pass

	def setDate(self, d):
		return d

	def changeYear(self):
		if self.status_button:
			print("true -")
			self.status_button = False

			if self.status_lef == "year":
				self.verticalFrameYear.deleteLater()
			elif self.status_lef == "month":
				self.verticalFrameMonth.deleteLater()

			print(self.status_lef)
			self.frameDay()
		else:
			print("false -")
			self.status_button = True
			self.verticalFrameDay.deleteLater()
			self.frameYear(self.today_now[2])

	def yearLeft(self):
		for key, value in self.buttons_years.items():
			value.buttonAdd().deleteLater()
		self.buttons_years = {}
		new_year = self.year_now - 20
		self.year_now = new_year
		self.reset_year = new_year
		self.calendarYears(new_year)

	def yearRight(self):
		for key, value in self.buttons_years.items():
			value.buttonAdd().deleteLater()
		self.buttons_years = {}
		new_year = self.year_now + 20
		self.year_now = new_year
		self.reset_year = new_year
		self.calendarYears(new_year)

	def dateLeft(self):
		for key, value in self.buttons_all.items():
			value[0].buttonGrid().deleteLater()
		self.buttons_all = {}
		if self.date_now[1] == 1:
			self.date_now = [1, 13, self.date_now[2] - 1]
		new_date = [1, self.date_now[1] - 1, self.date_now[2]]
		self.date_now = new_date
		self.calendarNumbers(new_date)

	def dateRight(self):
		for key, value in self.buttons_all.items():
			value[0].buttonGrid().deleteLater()
		self.buttons_all = {}
		if self.date_now[1] == 12:
			self.date_now = [1, 0, self.date_now[2] + 1]
		new_date = [1, self.date_now[1] + 1, self.date_now[2]]
		self.date_now = new_date
		self.calendarNumbers(new_date)

	def allLef(self):
		if self.status_lef == "day":
			self.dateLeft()
		elif self.status_lef == "month":
			self.empty()
		elif self.status_lef == "year":
			self.yearLeft()

	def allRight(self):
		if self.status_right == "day":
			self.dateRight()
		elif self.status_right == "month":
			self.empty()
		elif self.status_right == "year":
			self.yearRight()


class QButtonMonth():
	def __init__(self, name_month=None, size_font=None, central=None):
		self.name_month = name_month
		self.size_font = size_font
		self.central = central

		self.button_name = str(self.name_month.replace(' ', '_').lower()) + "_buttonMonth"
		self.font_standart = FontMaterial(self.size_font).fontSize()

		self.button_month = QtWidgets.QPushButton(self.central)
		self.button_month.setMinimumSize(QtCore.QSize(100, 28))
		self.button_month.setMaximumSize(QtCore.QSize(100, 28))
		self.button_month.setFont(self.font_standart)
		self.button_month.setStyleSheet("""
        	QPushButton {
	    		border-radius: 14px;
    			background: none;
			}
			QPushButton:hover {
    			background: #bebebe;
			}
			QPushButton:checked {
				background: #3f51b5;
    			color: #ffffff;
			}
		""")
		self.button_month.setText(self.name_month)
		self.button_month.setCheckable(True)
		# self.button_year.setChecked(False)
		self.button_month.setObjectName(self.button_name)

	def buttonAdd(self):
		return self.button_month

class QButtonYear():
	def __init__(self, name_year=None, size_font=None, central=None):
		self.name_year = name_year
		self.size_font = size_font
		self.central = central

		self.button_name = str(self.name_year.replace(' ', '_').lower()) + "_buttonYear"
		self.font_standart = FontMaterial(self.size_font).fontSize()

		self.button_year = QtWidgets.QPushButton(self.central)
		self.button_year.setMinimumSize(QtCore.QSize(56, 28))
		self.button_year.setMaximumSize(QtCore.QSize(56, 28))
		self.button_year.setFont(self.font_standart)
		self.button_year.setStyleSheet("""
        	QPushButton {
	    		border-radius: 14px;
    			background: none;
			}
			QPushButton:hover {
    			background: #bebebe;
			}
			QPushButton:checked {
				background: #3f51b5;
    			color: #ffffff;
			}
		""")
		self.button_year.setText(self.name_year)
		self.button_year.setCheckable(True)
		# self.button_year.setChecked(False)
		self.button_year.setObjectName(self.button_name)

	def buttonAdd(self):
		return self.button_year


class QButtonDate():
	def __init__(self, name_date=None, size_font=None, central=None, ud=None):
		self.name_date = name_date
		self.size_font = size_font
		self.central = central
		self.ud = ud

		self.button_name = str(self.name_date.replace(' ', '_').lower()) + "_button"

		self.font_standart = FontMaterial(self.size_font).fontSize()

		self.button_date = QtWidgets.QPushButton(self.central)
		self.button_date.setMinimumSize(QtCore.QSize(28, 28))
		self.button_date.setMaximumSize(QtCore.QSize(28, 28))
		self.button_date.setFont(self.font_standart)
		self.button_date.setStyleSheet("""
        	QPushButton {
	    		border-radius: 14px;
    			background: none;
			}
			QPushButton:hover {
    			background: #bebebe;
			}
			QPushButton:checked {
				background: #3f51b5;
    			color: #ffffff;
			}
		""")
		self.button_date.setObjectName(self.button_name)
		self.button_date.setText(self.name_date)

	def buttonGrid(self):
		return self.button_date

class QLabelDate():
	def __init__(self, name_label=None, size_font=None, central=None):
		self.name_label = name_label
		self.size_font = size_font
		self.central = central

		self.label_name = str(self.name_label.replace(' ', '_').lower()) + "_label"

		self.font_standart = FontMaterial(self.size_font).fontSize()
		self.font_standart.setWeight(56)
		self.label_date = QtWidgets.QLabel(self.central)
		self.label_date.setFont(self.font_standart)
		self.label_date.setStyleSheet("""
        	QLabel {
    			color: #a1a1a1;
    			font-weight: 450
			}
			""")
		self.label_date.setAlignment(QtCore.Qt.AlignCenter)
		self.label_date.setObjectName(self.label_name)
		self.label_date.setText(self.name_label)

	def labelGrid(self):
		return self.label_date