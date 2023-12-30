import sympy as sp
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('QtAgg')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import numpy as np


class Ui_Simpsons13(object):
    def setupUi(self, Simpsons13):
        Simpsons13.setObjectName("Simpsons13")
        Simpsons13.resize(498, 427)
        Simpsons13.setStyleSheet("/*\n"
"Material Dark Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Inspired on https://github.com/jxfwinter/qt-material-stylesheet\n"
"Company: GTRONICK\n"
"Last updated: 04/12/2018, 15:00.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/MaterialDark.qss\n"
"*/\n"
"QMainWindow {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QColorDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTextEdit {\n"
"    background-color:#1e1d23;\n"
"    color: #a9b7c6;\n"
"}\n"
"QPlainTextEdit {\n"
"    selection-background-color:#007b50;\n"
"    background-color:#1e1d23;\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"}\n"
"\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    padding: 0 8px;\n"
"    color: #a9b7c6;\n"
"    background:#1e1d23;\n"
"    selection-background-color:#007b50;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"QLabel {\n"
"    color: #a9b7c6;\n"
"}\n"
"QLCDNumber {\n"
"    color: #37e6b4;\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color:#1e1d23;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #04b97f;\n"
"    border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenuBar::item {\n"
"    color: #a9b7c6;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"      background: #1e1d23;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background:#1e1d23;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: #04b97f;\n"
"    border-bottom-color: transparent;\n"
"    border-left-width: 2px;\n"
"    color: #FFFFFF;\n"
"    padding-left:15px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu::item {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu{\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(77,77,77);\n"
"        background-color:#1e1d23;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding: 3px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-left: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: #04b97f;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: #04b97f;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QComboBox {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QComboBox:editable {\n"
"    background: #1e1d23;\n"
"    color: #a9b7c6;\n"
"    selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"    selection-color: #FFFFFF;\n"
"    selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QFontComboBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    height: 14px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: #04b97f;\n"
"}\n"
"/*split*/\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #100E19;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    background-color: #151a1e;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-width: 2px;\n"
"    border-radius: 1px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-width: 2px;\n"
"    border-radius: 1px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QStackedWidget {\n"
"    background-color: #1e1d23;\n"
"    border: 1px solid rgb(77, 77, 77);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QStackedWidget {\n"
"    background-color: #1e1d23;\n"
"    border: 1px solid rgb(77, 77, 77);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QStackedWidget::widget {\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QStackedWidget::widget:selected {\n"
"    background-color: #1e1d23;\n"
"    border-bottom: 2px solid #04b97f;\n"
"}\n"
"\n"
"QStackedWidget::widget:hover {\n"
"    border-bottom: 1px solid #04b97f;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Simpsons13)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(3, 3, 491, 421))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.resultTextBox1 = QtWidgets.QLineEdit(self.tab_3)
        self.resultTextBox1.setGeometry(QtCore.QRect(70, 240, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resultTextBox1.setFont(font)
        self.resultTextBox1.setReadOnly(True)
        self.resultTextBox1.setPlaceholderText("")
        self.resultTextBox1.setObjectName("resultTextBox1")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.startRangeTextBox = QtWidgets.QLineEdit(self.tab_3)
        self.startRangeTextBox.setGeometry(QtCore.QRect(70, 70, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startRangeTextBox.setFont(font)
        self.startRangeTextBox.setObjectName("startRangeTextBox")
        self.calculateButton1 = QtWidgets.QPushButton(self.tab_3)
        self.calculateButton1.setGeometry(QtCore.QRect(180, 310, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calculateButton1.setFont(font)
        self.calculateButton1.setObjectName("calculateButton1")
        self.functionTextBox = QtWidgets.QLineEdit(self.tab_3)
        self.functionTextBox.setGeometry(QtCore.QRect(70, 20, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.functionTextBox.setFont(font)
        self.functionTextBox.setObjectName("functionTextBox")
        self.endRangeTextBox = QtWidgets.QLineEdit(self.tab_3)
        self.endRangeTextBox.setGeometry(QtCore.QRect(70, 120, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.endRangeTextBox.setFont(font)
        self.endRangeTextBox.setObjectName("endRangeTextBox")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.intervalsTextBox = QtWidgets.QLineEdit(self.tab_3)
        self.intervalsTextBox.setGeometry(QtCore.QRect(70, 170, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.intervalsTextBox.setFont(font)
        self.intervalsTextBox.setObjectName("intervalsTextBox")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.xValuesTextBox = QtWidgets.QLineEdit(self.tab)
        self.xValuesTextBox.setGeometry(QtCore.QRect(80, 40, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.xValuesTextBox.setFont(font)
        self.xValuesTextBox.setObjectName("xValuesTextBox")
        self.yValuesTextBox = QtWidgets.QLineEdit(self.tab)
        self.yValuesTextBox.setGeometry(QtCore.QRect(80, 100, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yValuesTextBox.setFont(font)
        self.yValuesTextBox.setObjectName("yValuesTextBox")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(10, 230, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.calculateButton2 = QtWidgets.QPushButton(self.tab)
        self.calculateButton2.setGeometry(QtCore.QRect(180, 310, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calculateButton2.setFont(font)
        self.calculateButton2.setObjectName("calculateButton2")
        self.resultTextBox2 = QtWidgets.QLineEdit(self.tab)
        self.resultTextBox2.setGeometry(QtCore.QRect(80, 220, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resultTextBox2.setFont(font)
        self.resultTextBox2.setReadOnly(True)
        self.resultTextBox2.setPlaceholderText("")
        self.resultTextBox2.setObjectName("resultTextBox2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 471, 161))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_2, "")
        Simpsons13.setCentralWidget(self.centralwidget)
        self.retranslateUi(Simpsons13)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Simpsons13)
        self.calculateButton1.clicked.connect(lambda: self.simpsons_function(self.functionTextBox.text(),self.startRangeTextBox.text(),self.endRangeTextBox.text(),self.intervalsTextBox.text()))
        self.calculateButton1.clicked.connect(lambda: self.simpsons_function(self.functionTextBox.text(),self.startRangeTextBox.text(),self.endRangeTextBox.text(),self.intervalsTextBox.text()))

    def simpsons_function(self, func_str, a, b, n):
        self.resultTextBox1.setText("")
        if not func_str or not a or not b or not n:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Insufficient Input")
            msg.exec_()
            return

        x = sp.symbols('x')
        x_values = []
        y_values = []
        try:
            # Convert the input function string to a callable function
            func = sp.sympify(func_str)
        except sp.SympifyError:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Invalid function")
            msg.exec_()
            return

        try:
            # Convert the input range values to integers or floats
            a = float(a)
            b = float(b)
            n = int(n)
        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Invalid input for range or step")
            msg.exec_()
            return

        if n % 2 != 0:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Number of sub-intervals (n) should be even")
            msg.exec_()
            return

        # Calculate step size
        h = (b - a) / n

        # Simpson's rule formula
        integral = (h / 3) * (func.subs(x, a) + func.subs(x, b))

        x_values.append(a)
        y_values.append(float(func.subs(x, a)))

        for i in range(1, n):
            xi = a + i * h
            x_values.append(xi)
            y_values.append(float(func.subs(x, xi)))

            if i % 2 == 0:
                integral += (2 * h / 3) * func.subs(x, xi)
            else:
                integral += (4 * h / 3) * func.subs(x, xi)

        x_values.append(b)
        y_values.append(float(func.subs(x, b)))

        x_values_plot = np.linspace(a, b, 1000)  # Create a more refined set of x values
        y_values_plot = [float(func.subs(x, xi)) for xi in x_values_plot]  # Calculate y values for these x values

        self.resultTextBox1.setText(str(float(integral)))
        plt.plot(x_values_plot, y_values_plot, label="y(x)")  # Plot using the refined x and y values
        plt.legend()
        plt.show()
        return

    def constantDiff(self, arr):
        differences = np.diff(arr)
        constant_difference = np.allclose(differences, differences[0])
        return constant_difference

    def simpsons_table(self, x_values, y_values):
        self.resultTextBox2.setText("")
        if not x_values or not y_values:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Insufficient Input")
            msg.exec_()
            return
        x_values = list(map(float, x_values.split(',')))
        y_values = list(map(float, y_values.split(',')))
        if len(x_values) != len(y_values):
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("x and y values must have the same length")
            msg.exec_()
            return

        if len(x_values) % 2 == 0:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Number of x and y values should be odd")
            msg.exec_()
            return


        if not self.constantDiff(x_values):
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Difference between x values should be constant")
            msg.exec_()
            return

        h = (x_values[-1] - x_values[0]) / (len(x_values) - 1)

        integral = (h / 3) * (y_values[0] + y_values[-1])

        for i in range(1, len(x_values) - 1):
            if i % 2 == 0:
                integral += (2 * h / 3) * y_values[i]
            else:
                integral += (4 * h / 3) * y_values[i]

        self.resultTextBox2.setText(str(float(integral)))
        plt.plot(x_values, y_values, label="y(x)")
        plt.legend()
        plt.show()
        return
    def retranslateUi(self, Simpsons13):
        _translate = QtCore.QCoreApplication.translate
        Simpsons13.setWindowTitle(_translate("Simpsons13", "Simpson\'s 1/3"))
        self.label_6.setText(_translate("Simpsons13", "Result="))
        self.startRangeTextBox.setPlaceholderText(_translate("Simpsons13", "Enter the start of the range"))
        self.calculateButton1.setText(_translate("Simpsons13", "Calculate"))
        self.functionTextBox.setPlaceholderText(_translate("Simpsons13", "Enter the function"))
        self.endRangeTextBox.setPlaceholderText(_translate("Simpsons13", "Enter the end of the range"))
        self.label_7.setText(_translate("Simpsons13", "y(x)="))
        self.intervalsTextBox.setPlaceholderText(_translate("Simpsons13", "Enter the number of sub-intervals (even number)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Simpsons13", "Function"))
        self.xValuesTextBox.setPlaceholderText(_translate("Simpsons13", "Enter x values comma separated"))
        self.yValuesTextBox.setPlaceholderText(_translate("Simpsons13", "Enter y values comma separated"))
        self.label_8.setText(_translate("Simpsons13", "Result="))
        self.calculateButton2.setText(_translate("Simpsons13", "Calculate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Simpsons13", "Table"))
        self.label_5.setText(_translate("Simpsons13", "The Simpson\'s 1/3 rule is a numerical method used in calculus for approximating the definite integral of a function by dividing the area under the curve into multiple segments and applying quadratic approximations within each pair of segments using a polynomial interpolation formula. This rule is more accurate than the trapezoidal rule as it uses parabolic curves to estimate the integral."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Simpsons13", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Simpsons13 = QtWidgets.QMainWindow()
    ui = Ui_Simpsons13()
    ui.setupUi(Simpsons13)
    Simpsons13.show()
    sys.exit(app.exec_())
