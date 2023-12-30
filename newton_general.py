import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
#from sympy import Symbol
from PyQt5 import QtCore, QtGui, QtWidgets


class newton_general_Form(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1598, 757)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 590, 1591, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 40, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 0px;\n"
"border-style:inset;")
        self.label.setObjectName("label")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(70, 40, 91, 31))
        self.textBrowser_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(890, 40, 55, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 0px;\n"
"border-style:inset;")
        self.label_2.setObjectName("label_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(280, 40, 231, 31))
        self.textBrowser_3.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.textBrowser_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(210, 40, 55, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 0px;\n"
"border-style:inset;")
        self.label_3.setObjectName("label_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_4.setGeometry(QtCore.QRect(600, 40, 231, 31))
        self.textBrowser_4.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.textBrowser_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(540, 40, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 0px;\n"
"border-style:inset;")
        self.label_4.setObjectName("label_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_5.setGeometry(QtCore.QRect(960, 40, 231, 31))
        self.textBrowser_5.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 1px;\n"
"border-style:inset;\n"
"")
        self.textBrowser_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(1250, 40, 55, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 0px;\n"
"border-style:inset;")
        self.label_9.setObjectName("label_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_10.setGeometry(QtCore.QRect(1320, 40, 231, 31))
        self.textBrowser_10.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 1px;\n"
"border-style:inset;\n"
"")
        self.textBrowser_10.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_10.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_10.setObjectName("textBrowser_10")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 440, 1591, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(590, 30, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(1190, 30, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(560, 540, 231, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 1px;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 1591, 409))
        self.textBrowser.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1598, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
         #self.lineEdit.textEdited['QString'].connect(self.pushButton.click) # type: ignore
        #self.lineEdit_2.textEdited['QString'].connect(self.pushButton.click) # type: ignore
        #self.lineEdit_3.textEdited['QString'].connect(self.pushButton.click) # type: ignore
        #self.pushButton.clicked.connect(self.groupBox_2.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setStyleSheet("""
        /*
Material Dark Style Sheet for QT Applications
Author: Jaime A. Quiroga P.
Inspired on https://github.com/jxfwinter/qt-material-stylesheet
Company: GTRONICK
Last updated: 04/12/2018, 15:00.
Available at: https://github.com/GTRONICK/QSS/blob/master/MaterialDark.qss
*/
QMainWindow {
	background-color:#1e1d23;
}
QDialog {
	background-color:#1e1d23;
}
QColorDialog {
	background-color:#1e1d23;
}
QTextEdit {
	background-color:#1e1d23;
	color: #a9b7c6;
}
QPlainTextEdit {
	selection-background-color:#007b50;
	background-color:#1e1d23;
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-width: 1px;
	color: #a9b7c6;
}

QToolButton {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #04b97f;
	border-bottom-width: 1px;
	border-style: solid;
	color: #a9b7c6;
	padding: 2px;
	background-color: #1e1d23;
}
QToolButton:hover{
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #37efba;
	border-bottom-width: 2px;
	border-style: solid;
	color: #FFFFFF;
	padding-bottom: 1px;
	background-color: #1e1d23;
}

QLineEdit {
	border-width: 1px; border-radius: 4px;
	border-color: rgb(58, 58, 58);
	border-style: inset;
	padding: 0 8px;
	color: #a9b7c6;
	background:#1e1d23;
	selection-background-color:#007b50;
	selection-color: #FFFFFF;
}
QLabel {
	color: #a9b7c6;
}
QLCDNumber {
	color: #37e6b4;
}
QProgressBar {
	text-align: center;
	color: rgb(240, 240, 240);
	border-width: 1px; 
	border-radius: 10px;
	border-color: rgb(58, 58, 58);
	border-style: inset;
	background-color:#1e1d23;
}
QProgressBar::chunk {
	background-color: #04b97f;
	border-radius: 5px;
}
QMenuBar {
	background-color: #1e1d23;
}
QMenuBar::item {
	color: #a9b7c6;
  	spacing: 3px;
  	padding: 1px 4px;
  	background: #1e1d23;
}

QMenuBar::item:selected {
  	background:#1e1d23;
	color: #FFFFFF;
}
QMenu::item:selected {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: #04b97f;
	border-bottom-color: transparent;
	border-left-width: 2px;
	color: #FFFFFF;
	padding-left:15px;
	padding-top:4px;
	padding-bottom:4px;
	padding-right:7px;
	background-color: #1e1d23;
}
QMenu::item {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-bottom-width: 1px;
	border-style: solid;
	color: #a9b7c6;
	padding-left:17px;
	padding-top:4px;
	padding-bottom:4px;
	padding-right:7px;
	background-color: #1e1d23;
}
QMenu{
	background-color:#1e1d23;
}
QTabWidget {
	color:rgb(0,0,0);
	background-color:#1e1d23;
}
QTabWidget::pane {
		border-color: rgb(77,77,77);
		background-color:#1e1d23;
		border-style: solid;
		border-width: 1px;
    	border-radius: 6px;
}
QTabBar::tab {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-bottom-width: 1px;
	border-style: solid;
	color: #808086;
	padding: 3px;
	margin-left:3px;
	background-color: #1e1d23;
}
QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {
  	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #04b97f;
	border-bottom-width: 2px;
	border-style: solid;
	color: #FFFFFF;
	padding-left: 3px;
	padding-bottom: 2px;
	margin-left:3px;
	background-color: #1e1d23;
}

QCheckBox {
	color: #a9b7c6;
	padding: 2px;
}
QCheckBox:disabled {
	color: #808086;
	padding: 2px;
}

QCheckBox:hover {
	border-radius:4px;
	border-style:solid;
	padding-left: 1px;
	padding-right: 1px;
	padding-bottom: 1px;
	padding-top: 1px;
	border-width:1px;
	border-color: rgb(87, 97, 106);
	background-color:#1e1d23;
}
QCheckBox::indicator:checked {

	height: 10px;
	width: 10px;
	border-style:solid;
	border-width: 1px;
	border-color: #04b97f;
	color: #a9b7c6;
	background-color: #04b97f;
}
QCheckBox::indicator:unchecked {

	height: 10px;
	width: 10px;
	border-style:solid;
	border-width: 1px;
	border-color: #04b97f;
	color: #a9b7c6;
	background-color: transparent;
}
QRadioButton {
	color: #a9b7c6;
	background-color: #1e1d23;
	padding: 1px;
}
QRadioButton::indicator:checked {
	height: 10px;
	width: 10px;
	border-style:solid;
	border-radius:5px;
	border-width: 1px;
	border-color: #04b97f;
	color: #a9b7c6;
	background-color: #04b97f;
}
QRadioButton::indicator:!checked {
	height: 10px;
	width: 10px;
	border-style:solid;
	border-radius:5px;
	border-width: 1px;
	border-color: #04b97f;
	color: #a9b7c6;
	background-color: transparent;
}
QStatusBar {
	color:#027f7f;
}
QSpinBox {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QDoubleSpinBox {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QTimeEdit {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QDateTimeEdit {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QDateEdit {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QComboBox {
	color: #a9b7c6;	
	background: #1e1d23;
}
QComboBox:editable {
	background: #1e1d23;
	color: #a9b7c6;
	selection-background-color: #1e1d23;
}
QComboBox QAbstractItemView {
	color: #a9b7c6;	
	background: #1e1d23;
	selection-color: #FFFFFF;
	selection-background-color: #1e1d23;
}
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
	color: #a9b7c6;	
	background: #1e1d23;
}
QFontComboBox {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QToolBox {
	color: #a9b7c6;
	background-color: #1e1d23;
}
QToolBox::tab {
	color: #a9b7c6;
	background-color: #1e1d23;
}
QToolBox::tab:selected {
	color: #FFFFFF;
	background-color: #1e1d23;
}
QScrollArea {
	color: #FFFFFF;
	background-color: #1e1d23;
}
QSlider::groove:horizontal {
	height: 5px;
	background: #04b97f;
}
QSlider::groove:vertical {
	width: 5px;
	background: #04b97f;
}
QSlider::handle:horizontal {
	background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
	border: 1px solid #5c5c5c;
	width: 14px;
	margin: -5px 0;
	border-radius: 7px;
}
QSlider::handle:vertical {
	background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);
	border: 1px solid #5c5c5c;
	height: 14px;
	margin: 0 -5px;
	border-radius: 7px;
}
QSlider::add-page:horizontal {
    background: white;
}
QSlider::add-page:vertical {
    background: white;
}
QSlider::sub-page:horizontal {
    background: #04b97f;
}
QSlider::sub-page:vertical {
    background: #04b97f;
}
/*split*/
QPushButton{
	border-style: solid;
	border-color: #050a0e;
	border-width: 1px;
	border-radius: 5px;
	color: #d3dae3;
	padding: 2px;
	background-color: #100E19;
}
QPushButton::default{
	border-style: solid;
	border-color: #050a0e;
	border-width: 1px;
	border-radius: 5px;
	color: #FFFFFF;
	padding: 2px;
	background-color: #151a1e;
}
QPushButton:hover{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);
    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);
    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);
    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);
	border-width: 2px;
    border-radius: 1px;
	color: #d3dae3;
	padding: 2px;
}
QPushButton:pressed{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);
    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);
    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);
    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);
	border-width: 2px;
    border-radius: 1px;
	color: #d3dae3;
	padding: 2px;
}

QStackedWidget {
    background-color: #1e1d23;
    border: 1px solid rgb(77, 77, 77);
    border-radius: 6px;
}

QStackedWidget {
    background-color: #1e1d23;
    border: 1px solid rgb(77, 77, 77);
    border-radius: 6px;
}

QStackedWidget::widget {
    padding: 6px;
}

QStackedWidget::widget:selected {
    background-color: #1e1d23;
    border-bottom: 2px solid #04b97f;
}

QStackedWidget::widget:hover {
    border-bottom: 1px solid #04b97f;
}

    """)

        self.pushButton.clicked.connect(self.newton_inputs)

    def newton_inputs(self):
        delta1 = 0
        delta2 = 0      
        delta3 = 0
        delta4 = 0
        delta5 = 0
        X = [float(i) for i in self.lineEdit.text().split()]
        Y = [float(i) for i in self.lineEdit_2.text().split()]
        xvalue = float(self.lineEdit_3.text())
        X.sort(key=lambda x: abs(x - xvalue))
        Y = [x for _, x in sorted(zip(X, Y))]
        Y1 = Y[0]  # 1st element in Y

        list1 = []  # delta y list
        for i in range(len(X) - 1):
                T = (Y[i + 1] - Y[i]) / (X[i + 1] - X[i])
                list1.append(T)
                delta1 = list1[0]  # 1st element in delta y1

        list2 = []  # delta2 y list
        for i in range(len(X) - 2):
                T = (list1[i + 1] - list1[i]) / (X[i + 2] - X[i])
                list2.append(T)
                delta2 = list2[0]  # 1st element in delta2 y

        if (len(X) - 3 > 0):
                list3 = []  # delta3 y list
                for i in range(len(X) - 3):
                        T = (list2[i + 1] - list2[i]) / (X[i + 3] - X[i])
                        list3.append(T)
                        delta3 = list3[0]  # 1st element in delta3 y

        if (len(X) - 4 > 0):
                list4 = []  # delta4 y list
                for i in range(len(X) - 4):
                        T = (list3[i + 1] - list3[i]) / (X[i + 4] - X[i])
                        list4.append(T)
                        delta4 = list4[0]  # 1st element in delta4 y

        if (len(X) - 5 > 0):
                list5 = []
                for i in range(len(X) - 5):
                        T = (list4[i + 1] - list4[i]) / (X[i + 5] - X[i])
                        list5.append(T)
                        delta5 = list5[0]  # 1st element in delta5 y

        x = sp.Symbol('x')  # symbol for x
        fun = sp.Symbol('fun')  # symbol for f(x)
        symbol_y = sp.Symbol('symbol_y')  # symbol for y
        symbol_r = sp.Symbol('symbol_r')  # symbol for r

        if (delta5 != 0.0):
                y = Y1 + delta1 * (xvalue - X[0]) + delta2 * (xvalue - X[0]) * (xvalue - X[1]) + delta3 * (xvalue - X[0]) * (
                                 xvalue - X[1]) * (xvalue - X[2]) + delta4 * (xvalue - X[0]) * (xvalue - X[1]) * (xvalue - X[2]) * (
                                    xvalue - X[3])
                r = delta5 * (xvalue - X[0]) * (xvalue - X[1]) * (xvalue - X[2]) * (xvalue - X[3]) * (xvalue - X[4])
                symbol_y = Y1 + delta1 * (x - X[0]) + delta2 * (x - X[0]) * (x - X[1]) + delta3 * (x - X[0]) * (
                        x - X[1]) * (x - X[2]) + delta4 * (x - X[0]) * (x - X[1]) * (x - X[2]) * (x - X[3])
                symbol_r = delta5 * (x - X[0]) * (x - X[1]) * (x - X[2]) * (x - X[3]) * (x - X[4])

        if (delta5 == 0.0):
                y = Y1 + delta1 * (xvalue - X[0]) + delta2 * (xvalue - X[0]) * (xvalue - X[1]) + delta3 * (xvalue - X[0]) * (
                                xvalue - X[1]) * (xvalue - X[2])
                r = delta4 * (xvalue - X[0]) * (xvalue - X[1]) * (xvalue - X[2]) * (xvalue - X[3])
                symbol_y = Y1 + delta1 * (x - X[0]) + delta2 * (x - X[0]) * (x - X[1]) + delta3 * (x - X[0]) * (
                        x - X[1]) * (x - X[2])
                symbol_r = delta4 * (x - X[0]) * (x - X[1]) * (x - X[2]) * (x - X[3])

        if (delta4 == 0.0 and delta5 == 0.0):
                y = Y1 + delta1 * (xvalue - X[0]) + delta2 * (xvalue - X[0]) * (xvalue - X[1])
                r = delta3 * (xvalue - X[0]) * (xvalue - X[1]) * (xvalue - X[2])
                symbol_y = Y1 + delta1 * (x - X[0]) + delta2 * (x - X[0]) * (x - X[1])
                symbol_r = delta3 * (x - X[0]) * (x - X[1]) * (x - X[2])

        f = Y1 + delta1 * (xvalue - X[0]) + delta2 * (xvalue - X[0]) * (xvalue - X[1]) + delta3 * (xvalue - X[0]) * (
                xvalue - X[1]) * (xvalue - X[2]) + delta4 * (xvalue - X[0]) * (xvalue - X[1]) * (xvalue - X[2]) * (xvalue - X[3])

        fun = Y1 + delta1 * (x - X[0]) + delta2 * (x - X[0]) * (x - X[1]) + delta3 * (x - X[0]) * (
                x - X[1]) * (x - X[2]) + delta4 * (x - X[0]) * (x - X[1]) * (x - X[2]) * (x - X[3])

        if (delta5 != 0.0):
                f += delta5 * (xvalue - X[0]) * (xvalue - X[1]) * (xvalue - X[2]) * (xvalue - X[3]) * (xvalue - X[4])
                fun += delta5 * (x - X[0]) * (x - X[1]) * (x - X[2]) * (x - X[3]) * (x - X[4])
        fdashFormat = sp.diff(fun, x)  # fdash in symbols
        fdash = fdashFormat.subs({x: xvalue, fun: f})
        self.textBrowser_2.setText(str(xvalue))
        self.textBrowser_3.setText(str(y))
        self.textBrowser_4.setText(str(r))
        self.textBrowser_5.setText(str(f))
        self.textBrowser_10.setText(str(fdash))
        plt.plot(X, Y, marker='o', linestyle='', markersize=8, color='r')
        plt.plot(X, Y, color='tab:blue')
        plt.xlabel('X-Axis')
        plt.ylabel('Y-Axis')
        plt.title('Newton General Interpolation Plot')
        plt.legend()
        plt.show()



        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Results"))
        self.label.setText(_translate("MainWindow", "At x ="))
        self.label_2.setText(_translate("MainWindow", "F(X) ="))
        self.label_3.setText(_translate("MainWindow", "Y(X) ="))
        self.label_4.setText(_translate("MainWindow", "R(X) ="))
        self.label_9.setText(_translate("MainWindow", "F\'(X) ="))
        self.groupBox.setTitle(_translate("MainWindow", "Input"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter X elements separated by spaces"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter Y elements separated by spaces"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Enter Value of X to get Y(X)"))
        self.pushButton.setText(_translate("MainWindow", "Proceed"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">HOW IT WORKS:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\"><br />Data Input</span><span style=\" font-size:10pt;\">: The code prompts the user to input values for X and Y coordinates and a specific x-value for interpolation.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Sorting</span><span style=\" font-size:10pt;\">: It sorts the X values and rearranges the Y values based on the sorted order of the X values.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Calculating Differences</span><span style=\" font-size:10pt;\">: It calculates divided differences (delta1, delta2,...) using the divided difference formula for interpolating polynomials.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Interpolation</span><span style=\" font-size:10pt;\">: Using the Newton interpolation formula, it computes the polynomial function f and symbolic expressions (fun, symbol_y, symbol_r) for interpolation, residual error, and the interpolated value at the specified x-value.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Derivative Calculation</span><span style=\" font-size:10pt;\">: It computes the derivative of the interpolated function at the specified x value.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Plotting</span><span style=\" font-size:10pt;\">: Lastly, it plots the original data points and the interpolated polynomial.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">What to avoid:</span><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">-Extremely Large or small input values will cause numerical instability.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">-Duplicate values for X are NOT allowed. That repetition will cause division by zero.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = newton_general_Form()
    ui.setupUi(MainWindow)
        
    MainWindow.show()
    sys.exit(app.exec_())
