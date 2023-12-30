import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import matplotlib
matplotlib.use('QtAgg')


class Ui_CurveFittingForm(object):
    def setupUi(self, CurveFittingForm):
        CurveFittingForm.setObjectName("CurveFittingForm")
        CurveFittingForm.resize(446, 566)
        CurveFittingForm.setStyleSheet("/*\n"
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
        self.centralwidget = QtWidgets.QWidget(CurveFittingForm)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(3, 3, 440, 560))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.functionTextBox = QtWidgets.QLineEdit(self.tab)
        self.functionTextBox.setGeometry(QtCore.QRect(70, 30, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.functionTextBox.setFont(font)
        self.functionTextBox.setObjectName("functionTextBox")
        self.xValuesTextBox = QtWidgets.QLineEdit(self.tab)
        self.xValuesTextBox.setGeometry(QtCore.QRect(70, 80, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.xValuesTextBox.setFont(font)
        self.xValuesTextBox.setObjectName("xValuesTextBox")
        self.yValuesTextBox = QtWidgets.QLineEdit(self.tab)
        self.yValuesTextBox.setGeometry(QtCore.QRect(70, 130, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yValuesTextBox.setFont(font)
        self.yValuesTextBox.setObjectName("yValuesTextBox")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 230, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.aTextBox = QtWidgets.QLineEdit(self.tab)
        self.aTextBox.setGeometry(QtCore.QRect(70, 220, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aTextBox.setFont(font)
        self.aTextBox.setReadOnly(True)
        self.aTextBox.setPlaceholderText("")
        self.aTextBox.setObjectName("aTextBox")
        self.bTextBox = QtWidgets.QLineEdit(self.tab)
        self.bTextBox.setGeometry(QtCore.QRect(70, 280, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bTextBox.setFont(font)
        self.bTextBox.setReadOnly(True)
        self.bTextBox.setPlaceholderText("")
        self.bTextBox.setObjectName("bTextBox")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 290, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(40, 350, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cTextBox = QtWidgets.QLineEdit(self.tab)
        self.cTextBox.setGeometry(QtCore.QRect(70, 340, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cTextBox.setFont(font)
        self.cTextBox.setReadOnly(True)
        self.cTextBox.setPlaceholderText("")
        self.cTextBox.setObjectName("cTextBox")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(40, 410, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.rTextBox = QtWidgets.QLineEdit(self.tab)
        self.rTextBox.setGeometry(QtCore.QRect(70, 400, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rTextBox.setFont(font)
        self.rTextBox.setReadOnly(True)
        self.rTextBox.setPlaceholderText("")
        self.rTextBox.setObjectName("rTextBox")
        self.calculateButton = QtWidgets.QPushButton(self.tab)
        self.calculateButton.setGeometry(QtCore.QRect(150, 470, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calculateButton.setFont(font)
        self.calculateButton.setObjectName("calculateButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 411, 331))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_2, "")
        CurveFittingForm.setCentralWidget(self.centralwidget)
        self.retranslateUi(CurveFittingForm)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CurveFittingForm)
        self.calculateButton.clicked.connect(lambda: self.CurveFitting(self.functionTextBox.text(), self.xValuesTextBox.text(), self.yValuesTextBox.text()))

    def CurveFitting(self, expression, x_data_string, y_data_string):
            self.aTextBox.setText("")
            self.bTextBox.setText("")
            self.cTextBox.setText("")
            self.rTextBox.setText("")
            if not expression or not x_data_string or not y_data_string:
                    msg = QMessageBox()
                    msg.setWindowTitle("ERROR")
                    msg.setText("Insufficient Input")
                    msg.exec_()
                    return

            def curve(x, a, b, c):
                    return eval(expression)

            x_array = x_data_string.split()
            x_data1 = [float(element) for element in x_array]
            x_data = np.array(x_data1)
            y_array = y_data_string.split()
            y_data1 = [float(element) for element in y_array]
            y_data = np.array(y_data1)

            params, covariance = curve_fit(curve, x_data, y_data)
            # a , b , c
            a_fit, b_fit, c_fit = params

            self.aTextBox.setText(str(a_fit))
            self.bTextBox.setText(str(b_fit))
            self.cTextBox.setText(str(c_fit))

            # Fitted y values
            y_fit = curve(x_data, a_fit, b_fit, c_fit)

            correlation_matrix = np.corrcoef(y_data, y_fit)
            # Correlation coefficient
            correlation_coefficient = correlation_matrix[0, 1]

            self.rTextBox.setText(str(correlation_coefficient))

            # Plotting

            plt.plot(x_data, y_data, label='Data')
            plt.plot(x_data, y_fit, label='Fitted Data')
            plt.legend()
            plt.show()

    def retranslateUi(self, CurveFittingForm):
        _translate = QtCore.QCoreApplication.translate
        CurveFittingForm.setWindowTitle(_translate("CurveFittingForm", "Curve Fitting"))
        self.functionTextBox.setPlaceholderText(_translate("CurveFittingForm", "Enter the function"))
        self.xValuesTextBox.setPlaceholderText(_translate("CurveFittingForm", "Enter x values space separated"))
        self.yValuesTextBox.setPlaceholderText(_translate("CurveFittingForm", "Enter y values space separated"))
        self.label.setText(_translate("CurveFittingForm", "a="))
        self.label_2.setText(_translate("CurveFittingForm", "b="))
        self.label_3.setText(_translate("CurveFittingForm", "c="))
        self.label_4.setText(_translate("CurveFittingForm", "r="))
        self.calculateButton.setText(_translate("CurveFittingForm", "Calculate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("CurveFittingForm", "Calculator"))
        self.label_5.setText(_translate("CurveFittingForm", "Curve fitting is a numerical technique that aims to determine a suitable mathematical function that represents a set of data points. It approximates the relationship between the independent variable (x) and the dependent variable (y) within a data set. Curve fitting methods include:\n"
"\n"
"- Linear Regression  for linear relationships \n"
"- Polynomial Regression for flexible curve fitting\n"
"- Non-linear regression when above two are insufficient \n"
"- Splines for abrupt changes      \n"
"\n"
"Key considerations during curve fitting involve addressing overfitting, underfitting, and selecting an appropriate model complexity to ensure accurate representation and generalization to new data."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("CurveFittingForm", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurveFittingForm = QtWidgets.QMainWindow()
    ui = Ui_CurveFittingForm()
    ui.setupUi(CurveFittingForm)
    CurveFittingForm.show()
    sys.exit(app.exec_())
