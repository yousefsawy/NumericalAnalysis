
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sympy as sp
from sympy import sympify
from numericall import NonLinearNewton
from NewtonRaphson import Newton
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('QtAgg')

class NewtonRaphson1(QMainWindow):
    def clickediterations(self):
        self.ui.label_5.setVisible(True)
        self.ui.textEdit_5.setVisible(True)
        self.ui.label_6.setVisible(False)
        self.ui.textEdit_6.setVisible(False)
    def clickedstoppingerror(self):
        self.ui.label_6.setVisible(True)
        self.ui.textEdit_6.setVisible(True)
        self.ui.label_5.setVisible(False)
        self.ui.textEdit_5.setVisible(False)
    def __init__(self):
        super().__init__()
        self.OpenNewtonRaphson()
        #self.ui.pushButton_42.clicked.connect(self.VerifyFunc)
        self.ui.textEdit_5.setVisible(False)
        self.ui.textEdit_6.setVisible(False)
        self.ui.label_6.setVisible(False)
        self.ui.label_5.setVisible(False)
        self.ui.pushButton_2.clicked.connect(self.clickediterations)
        self.ui.pushButton_3.clicked.connect(self.clickedstoppingerror)
        self.ui.pushButton.clicked.connect(self.Get_result)






    def OpenNewtonRaphson(self):
        self.ui = Newton()
        self.ui.setupUi(self)

    def Get_result(self):
                input1=self.ui.textEdit.toPlainText()
                input2=self.ui.textEdit_2.toPlainText()
                input3= float (self.ui.textEdit_3.toPlainText())
                input4=float (self.ui.textEdit_4.toPlainText())
                if(self.ui.textEdit_6.toPlainText()):
                    input6=float (self.ui.textEdit_6.toPlainText())
                else:
                    input6=0
                if(self.ui.textEdit_5.toPlainText()):
                    input5=int (self.ui.textEdit_5.toPlainText())
                else:
                    input5=20
                output= []
                output=NonLinearNewton(input1,input2,input3,input4,input5,input6)
                self.ui.textEdit_7.setText(str(output[0]))
                self.ui.textEdit_8.setText(str(output[1]))
                self.ui.textEdit_9.setText(str(output[2]))
                self.ui.textEdit_10.setText(str(output[3]))




if __name__ == "__main__":
        app = QApplication([])
        window =NewtonRaphson1()
        window.show()
        app.exec_()