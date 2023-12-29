import sys
from sympy import sympify, symbols
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QColor  # Corrected import statement
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from UI_RK import Ui_Widget
from RK_Logic import Runge_Kutta


class RK_UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.OpenRK()
        self.ui.frame.setVisible(False)
        self.ui.pushButton_2.clicked.connect(self.initInput)
        self.ui.pushButton_10.clicked.connect(self.executeFunc)
        self.ui.pushButton_9.clicked.connect(self.handleInfo)
        
    def DisableSecond(self):
        self.ui.lineEdit_10.setEnabled(False)
        self.ui.lineEdit_4.setEnabled(False)
        self.ui.lineEdit_12.setEnabled(False)
        self.ui.lineEdit_10.setStyleSheet("background-color: rgb(82, 90, 100);")
        self.ui.lineEdit_4.setStyleSheet("background-color: rgb(82, 90, 100);")
        self.ui.lineEdit_12.setStyleSheet("background-color: rgb(82, 90, 100);")

    def EnableSecond(self):
        self.ui.lineEdit_10.setEnabled(True)
        self.ui.lineEdit_4.setEnabled(True)
        self.ui.lineEdit_12.setEnabled(True)
        self.ui.lineEdit_10.setStyleSheet("background-color: transparent;")
        self.ui.lineEdit_4.setStyleSheet("background-color: transparent;")
        self.ui.lineEdit_12.setStyleSheet("background-color: transparent;")

    def handleInfo(self):
        self.ui.frame.setVisible(not self.ui.frame.isVisible())    
                
    def OpenRK(self):
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    def initInput(self):
        self.ValidateInputN()
        if (self.N ==1):
            self.DisableSecond()
        else:
            self.EnableSecond()
        self.initInputVector()

    def ValidateInputN(self):
        try:
            self.N = int(self.ui.lineEdit_5.text())
            if (self.N<1 or self.N>2):
                raise Exception("Enter 1 or 2")
        except:
            self.show_warning_messagebox('N should be a positive integer (1 or 2)')
        
    def initInputVector(self):
        self.ui.tableWidget_7.setColumnCount(self.N+1)
        self.ui.tableWidget_7.setRowCount(1)
        self.ui.tableWidget_7.verticalHeader().setVisible(False)
        self.ui.tableWidget_7.horizontalHeader().setVisible(False) 
        for col in range(self.N+1):
            item = QTableWidgetItem('')
            self.ui.tableWidget_7.setItem(0, col, item)
            self.ui.tableWidget_7.setColumnWidth(col, int(250/(self.N)))

    def ValidateVectorInput(self):
        self.vector = [0]*(self.N+1)
        try:
            for col in range(self.N+1):
                self.vector[col]=(float(self.ui.tableWidget_7.item(0, col).text()))
        except:
            self.show_warning_messagebox('Invalid Vector Input')

    def validateFunctions(self):
        try:
            self.func=[]
            self.exact=[]
            x, y, z = symbols('x y z')
            sympified_expr = sympify(self.ui.lineEdit_7.text(), locals={'x': x, 'y': y, 'z': z})
            self.func.append(self.ui.lineEdit_7.text())
            sympified_expr = sympify(self.ui.lineEdit_6.text(), locals={'x': x, 'y': y, 'z': z})
            self.exact.append(self.ui.lineEdit_6.text())
            if (self.N==2):
                sympified_expr = sympify(self.ui.lineEdit_4.text(), locals={'x': x, 'y': y, 'z': z})
                self.func.append(self.ui.lineEdit_4.text())
                sympified_expr = sympify(self.ui.lineEdit_10.text(), locals={'x': x, 'y': y, 'z': z})
                self.func.append(self.ui.lineEdit_10.text())
        except:
            self.show_warning_messagebox("Invalid Expression.")

    def ValidateX1(self):
        try:
            self.X1 = float(self.ui.lineEdit_9.text())
        except:
            self.show_warning_messagebox('X1 should be a valid Number')

        
    def executeFunc(self):
        self.validateFunctions()
        self.ValidateVectorInput()
        self.ValidateX1()
        y,True_Error = Runge_Kutta(self.func, self.exact, self.X1, self.vector)
        self.ui.lineEdit_11.setText(str(y[2]))
        if (self.N==2):
            self.ui.lineEdit_12.setText(str(y[1]))
        self.ui.lineEdit_13.setText(str(True_Error[0]))


    
    def show_warning_messagebox(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Wrong Input")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = msg.exec_()



def RK():
    app = QApplication([])
    window = RK_UI()
    window.show()
    app.exec_()

if __name__ == '__main__':
    RK()