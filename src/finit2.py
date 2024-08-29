from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Finite_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1124, 560)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(440, 380, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 1111, 231))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 250, 1091, 121))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width: 1.1;\n"
"border-style:inset;\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 50, 251, 31))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(320, 50, 131, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(530, 50, 113, 31))
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(720, 50, 113, 31))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(920, 50, 113, 31))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 430, 1091, 121))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width: 1.1;\n"
"border-style:inset;\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(450, 40, 181, 41))
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        Form.setStyleSheet

        self.pushButton.clicked.connect(self.calculateDerivative)

    def calculateDerivative(self):
        try:
            f = lambda x: eval(self.lineEdit_3.text())
            derivativeOrder = int(self.lineEdit_4.text())
            x = float(self.lineEdit_5.text())
            hMin = float(self.lineEdit_2.text())
            hOrder = int(self.lineEdit.text())

            result = self.finiteDifference(f, derivativeOrder, x, hMin, hOrder)
            self.lineEdit_6.setText(str(result))
        except Exception as e:
            print(f"Error: {e}")

    def finiteDifference(self,f,derivativeOrder,x,hMin,hOrder):
      print('We are going to calculate the derivative of f(x) at the entered value of x. Finite difference formulae produce approximate results for the value of the derivative. They are commonly used when the function is difficult to differentiate, and the speed of calculation is prioritised over the accuracy of the result. Nevertheless, a finite difference formula can still produce highly accurate results, when a suitable value for hMin is used.')
      if derivativeOrder == 1:
        if hOrder == 2:
            return (4 * f(x + hMin) - 3 * f(x) - f(x + 2 * hMin)) / (2 * hMin)
        elif hOrder == 4:
            h = [2 * hMin, hMin]
            table = []
            for i in range(2):
                table.append((4 * f(x + h[i]) - 3 * f(x) - f(x + 2 * h[i])) / (2 * h[i]))
            return (4 * table[1] - table[0]) / 3
        elif hOrder == 6:
            h = [4 * hMin, 2 * hMin, hMin]
            table = []
            for i in range(3):
                table.append((4 * f(x + h[i]) - 3 * f(x) - f(x + 2 * h[i])) / (2 * h[i]))
            for i in range(2):
                table.append((4 * table[i + 1] - table[i]) / 3)
            return (16 * table[4] - table[3]) / 15
        elif hOrder == 8:
            h = [8 * hMin, 4 * hMin, 2 * hMin, hMin]
            table = []
            for i in range(4):
                table.append((4 * f(x + h[i]) - 3 * f(x) - f(x + 2 * h[i])) / (2 * h[i]))
            for i in range(3):
                table.append((4 * table[i + 1] - table[i]) / 3)
            for i in range(2):
                table.append((16 * table[i + 5] - table[i + 4]) / 15)
            return (64 * table[8] - table[7]) / 63
      elif derivativeOrder == 2:
        if hOrder == 2:
            return (f(x + hMin) - 2 * f(x) + f(x - hMin)) / (hMin ** 2)
        elif hOrder == 4:
            h = [2 * hMin, hMin]
            table = []
            for i in range(2):
                table.append((f(x + h[i]) - 2 * f(x) + f(x - h[i])) / (h[i] ** 2))
            return (4 * table[1] - table[0]) / 3
        elif hOrder == 6:
            h = [4 * hMin, 2 * hMin, hMin]
            table = []
            for i in range(3):
                table.append((f(x + h[i]) - 2 * f(x) + f(x - h[i])) / (h[i] ** 2))
            for i in range(2):
                table.append((4 * table[i + 1] - table[i]) / 3)
            return (16 * table[4] - table[3]) / 15
        elif hOrder == 8:
            h = [8 * hMin, 4 * hMin, 2 * hMin, hMin]
            table = []
            for i in range(4):
                table.append((f(x + h[i]) - 2 * f(x) + f(x - h[i])) / (h[i] ** 2))
            for i in range(3):
                table.append((4 * table[i + 1] - table[i]) / 3)
            for i in range(2):
                table.append((16 * table[i + 5] - table[i + 4]) / 15)
            return (64 * table[8] - table[7]) / 63

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Continue"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline; color:#000000;\">About Section</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; text-decoration: underline; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">-\'f\' is the function whose derivative is required to be calculated.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">-\'derivativeOrder\' is the desired derivative order. It should be 1 (first derivative) or 2 (second derivative).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">-\'x\' is the value at which the derivative is calculated.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">-\'hMin\' is the minimum difference between two successive points to use in the formula.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">-\'hOrder\' is the order of the error of this solution. It should be 2 for O(h^2), 4 for O(h^4), 6 for O(h^6), or 8 for O(h^8)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">-We are going to calculate the derivative of f(x) at the entered value of x. Finite difference formulae produce approximate results for the value of the derivative. They are commonly used when the function is difficult to differentiate, and the speed of calculation is prioritised over the accuracy of the result. Nevertheless, a finite difference formula can still produce highly accurate results, when a suitable value for hMin is used.</span></p></body></html>"))
        self.groupBox.setTitle(_translate("Form", "Inputs"))
        self.groupBox.setTitle(_translate("Form", "Inputs"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Enter Function"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Enter Derivative order"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Enter x"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter Order Of H"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Enter H(min)"))
        self.groupBox_2.setTitle(_translate("Form", "Outputs"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "Result"))
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Finite_Form()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowTitle("Finite Difference")
    sys.exit(app.exec_())

