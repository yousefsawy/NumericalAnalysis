# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1029, 867)
        Widget.setStyleSheet("QMainWindow {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QWidget {\n"
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
"QPushButton{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    border-radius:4px;\n"
"    background-color: rgb(46, 45, 55);\n"
"}\n"
"QPushButton::default{\n"
"    border-style: inset;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
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
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 2px;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #37efba;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #808086;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-color: rgb(132, 144, 158);\n"
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
"QTableWidget\n"
"{\n"
"    border:1px solid rgb(132, 144, 158);\n"
"    border-radius: 4px;\n"
"    gridline-color:rgb(132, 144, 158);\n"
"}")
        self.pushButton_10 = QtWidgets.QPushButton(Widget)
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setGeometry(QtCore.QRect(450, 410, 66, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_9 = QtWidgets.QPushButton(Widget)
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setGeometry(QtCore.QRect(220, 50, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(30, 40, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Widget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 520, 491, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridLayoutWidget_2.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget_2.setSizePolicy(sizePolicy)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_4.addWidget(self.lineEdit_11, 0, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 1, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_4.addWidget(self.lineEdit_12, 1, 1, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_4.addWidget(self.lineEdit_13, 2, 1, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(Widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 130, 491, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridLayoutWidget.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget.setSizePolicy(sizePolicy)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 6, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 1, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_5.addWidget(self.lineEdit_6, 5, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_5.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 4, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_5.addWidget(self.lineEdit_7, 1, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 5, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_5.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 7, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 0, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_5.addWidget(self.lineEdit_9, 7, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_5.addWidget(self.lineEdit_5, 0, 1, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_5.addWidget(self.lineEdit_10, 6, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 3, 0, 1, 1)
        self.tableWidget_7 = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_7.sizePolicy().hasHeightForWidth())
        self.tableWidget_7.setSizePolicy(sizePolicy)
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(0)
        self.tableWidget_7.setRowCount(0)
        self.gridLayout_5.addWidget(self.tableWidget_7, 3, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(Widget)
        self.label_16.setGeometry(QtCore.QRect(30, 450, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.frame = QtWidgets.QFrame(Widget)
        self.frame.setGeometry(QtCore.QRect(580, 50, 391, 681))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"    Background:rgb(46, 45, 55);\n"
"    border-radius:4px\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_62 = QtWidgets.QLabel(self.frame)
        self.label_62.setGeometry(QtCore.QRect(20, 20, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_62.setFont(font)
        self.label_62.setObjectName("label_62")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(20, 70, 341, 631))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.plainTextEdit_5.setFont(font)
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.pushButton_10.setText(_translate("Widget", "Calculate "))
        self.pushButton_9.setText(_translate("Widget", "i"))
        self.label.setText(_translate("Widget", "Runge Kutta"))
        self.label_10.setText(_translate("Widget", "True Error="))
        self.label_9.setText(_translate("Widget", "Y ="))
        self.label_20.setText(_translate("Widget", "Z ="))
        self.label_19.setText(_translate("Widget", "Y="))
        self.label_14.setText(_translate("Widget", "dy/dx = "))
        self.label_13.setText(_translate("Widget", "dz/dx ="))
        self.label_17.setText(_translate("Widget", "Exact  Systems:"))
        self.label_18.setText(_translate("Widget", "Y="))
        self.pushButton_2.setText(_translate("Widget", "Initialize Input"))
        self.label_11.setText(_translate("Widget", "x1="))
        self.label_15.setText(_translate("Widget", "No. of Equations (Max 2)"))
        self.label_12.setText(_translate("Widget", "Initial Vector = "))
        self.label_16.setText(_translate("Widget", "Results"))
        self.label_62.setText(_translate("Widget", "About"))
        self.plainTextEdit_5.setPlainText(_translate("Widget", "Runge-Kutta is a numerical technique employed for the approximation of solutions to ordinary differential equations (ODEs), particularly those governing the dynamic behavior of systems evolving over time. Instead of providing an exact solution, Runge-Kutta methods offer a numerical approximation by iteratively computing the values of the solution at discrete time points.\n"
"\n"
"Among the various variants of the Runge-Kutta method, the fourth-order Runge-Kutta (RK4) is commonly utilized due to its balance between computational simplicity and accuracy. This method involves the evaluation of the system\'s governing equations at multiple intermediate points within each time step and then combining these evaluations to calculate the next value of the solution.\n"
"\n"
"The RK4 method specifically employs four function evaluations to obtain a weighted average, resulting in a more accurate approximation compared to lower-order methods. This makes RK4 well-suited for a broad spectrum of applications in diverse scientific and engineering domains.\n"
"\n"
"One key advantage of Runge-Kutta methods, including RK4, is their versatility in handling both stiff and non-stiff ODEs. Stiff ODEs pose challenges for many numerical methods, but RK4\'s robustness makes it a preferred choice for simulations involving a wide range of dynamic systems.\n"
"\n"
"In summary, Runge-Kutta methods, exemplified by RK4, represent indispensable tools in numerical analysis, offering practical and efficient solutions for approximating the behavior of dynamic systems in fields such as physics, engineering, biology, and more.\n"
"\n"
""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())