

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sympy as sp
from sympy import sympify
from Fixed_Point_V2 import fixed_point_main, fixed_point_1var, fixed_point_2var, plot_eqn
from FixedPoint import FixedPoint

class MainWindow(QMainWindow):
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
        self.OpenFixedPoint()
        #self.ui.pushButton_42.clicked.connect(self.VerifyFunc)
        self.ui.textEdit_5.setVisible(False)
        self.ui.textEdit_6.setVisible(False)
        self.ui.label_6.setVisible(False)
        self.ui.label_5.setVisible(False)
        self.ui.pushButton_2.clicked.connect(self.clickediterations)
        self.ui.pushButton_3.clicked.connect(self.clickedstoppingerror)
        self.ui.pushButton.clicked.connect(self.Get_result)






    def OpenFixedPoint(self):
        self.ui = FixedPoint()
        self.ui.setupUi(self)

    def Get_result(self):
                input1=self.ui.textEdit.toPlainText()
                if(self.ui.textEdit_2.toPlainText()):
                    input2= (self.ui.textEdit_2.toPlainText())
                    input8=False
                else:
                    input2=0
                    input8=True
                input3= float (self.ui.textEdit_3.toPlainText())
                if(self.ui.textEdit_4.toPlainText()):
                    input4=float (self.ui.textEdit_4.toPlainText())
                else:
                    input4=0
                if(self.ui.textEdit_6.toPlainText()):
                    input6=float (self.ui.textEdit_6.toPlainText())
                else:
                    input6=0
                if(self.ui.textEdit_5.toPlainText()):
                    input5=int (self.ui.textEdit_5.toPlainText())
                    input7=True
                else:
                    input5=100
                    input7=False
                output= []
                output=fixed_point_main(input1,input2,input3,input4,input5,input6,input7,input8)
                if(len(output)==6):
                    self.ui.textEdit_7.setText(str(output[0]))
                    self.ui.textEdit_8.setText(str(output[1]))
                    self.ui.textEdit_9.setText(str(output[2]))
                    self.ui.textEdit_10.setText(str(output[3]))
                    self.ui.textEdit_11.setText(str(output[4]))
                    self.ui.textEdit_12.setText(str(output[5]))
                else:
                    self.ui.textEdit_7.setText(str(output[0]))
                    self.ui.textEdit_8.setText(str("NO"))
                    self.ui.textEdit_9.setText(str(output[1]))
                    self.ui.textEdit_10.setText(str("NO"))
                    self.ui.textEdit_11.setText(str(output[2]))
                    self.ui.textEdit_12.setText(str("NO"))
                plot_eqn(input1,input2,input8)


                #self.pushButton.clicked.connect(Get_result)



if __name__ == "__main__":
        app = QApplication([])
        window = MainWindow()
        window.show()
        app.exec_()
