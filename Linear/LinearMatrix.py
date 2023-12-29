import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from Linear.linear import Ui_Widget
from Linear.linear_logic import func


class LinearMatrix(QMainWindow):

    def __init__(self):
        super().__init__()
        self.OpenLinear()
        self.ui.frame.setVisible(False)
        self.ui.pushButton.clicked.connect(self.initInput)
        self.ui.pushButton_10.clicked.connect(self.executeFunc)
        self.ui.pushButton_9.clicked.connect(self.handleInfo)

    def handleInfo(self):
        self.ui.frame.setVisible(not self.ui.frame.isVisible())    
                
    def OpenLinear(self):
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    def initInput(self):
        self.ValidateInputN()
        self.initInputMatrix()
        self.initInputVector()

    def ValidateInputN(self):
        try:
            self.N = int(self.ui.lineEdit.text())
        except:
            self.show_warning_messagebox('N should be an integer')
            return
        
    def initInputMatrix(self):
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.horizontalHeader().setVisible(False)  
        self.InitRowsAndColumns()

    def InitRowsAndColumns(self):
        self.ui.tableWidget.setColumnCount(self.N+1)
        self.ui.tableWidget.setRowCount(self.N)
        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                item = QTableWidgetItem('')
                self.ui.tableWidget.setItem(row, col, item)
            self.ui.tableWidget.setRowHeight(row,int(190/self.N))
        
        for col in range(self.ui.tableWidget.columnCount()):
            self.ui.tableWidget.setColumnWidth(col, int(250 / (self.N + 1)))
        
    def initInputVector(self):
        self.ui.tableWidget_2.setColumnCount(self.N)
        self.ui.tableWidget_2.setRowCount(1)
        self.ui.tableWidget_2.verticalHeader().setVisible(False)
        self.ui.tableWidget_2.horizontalHeader().setVisible(False) 
        for col in range(self.ui.tableWidget_2.columnCount()):
            item = QTableWidgetItem('')
            self.ui.tableWidget_2.setItem(0, col, item)
            self.ui.tableWidget_2.setColumnWidth(col, int(250/(self.N)))
    
    def ValidateMatrixInputs(self):
        self.matrix = []
        try:
            for row in range(self.N):
                OneRow = []
                for col in range(self.N + 1):
                    print(self.ui.tableWidget.item(row, col).text())
                    OneRow.append(float(self.ui.tableWidget.item(row, col).text()))
                self.matrix.append(OneRow)
        except:
            self.show_warning_messagebox('Invalid Matrix Input')
            return
        
    def ValidateVectorInputs(self):
        self.vector = [0]*self.N
        try:
            for col in range(self.N):
                self.vector[col]=(float(self.ui.tableWidget.item(0, col).text()))
                print(self.vector[col])
        except:
            self.show_warning_messagebox('Invalid Vector Input')
            return
        
    def ValidateW(self):
        try:
            self.w = float(self.ui.lineEdit_3.text())
            if (self.w<1 or self.w>2):
                raise Exception("N should be an number between 1 & 2")
        except:
            self.show_warning_messagebox('N should be a number between 1 & 2')
            return
    
    def ValidateIterations(self):
        try:
            self.iterations = int(self.ui.lineEdit_2.text())
        except:
            self.show_warning_messagebox('iterations number should be an integer')
            return

    def ValidateInput(self):
        self.ValidateMatrixInputs()
        self.ValidateVectorInputs()
        self.ValidateW()
        self.ValidateIterations()


    def executeFunc(self):
        self.ValidateInput()
        self.error=[0] * self.N
        print (self.matrix)
        print (self.vector)
        self.finalVect= func(self.N, self.vector, self.matrix, self.iterations, self.w, self.error)
        self.ShowFinalVect()
        self.ShowFinalErrors()
    
    def ShowFinalVect(self):
        self.ui.tableWidget_3.setColumnCount(self.N)
        self.ui.tableWidget_3.setRowCount(1)
        self.ui.tableWidget_3.verticalHeader().setVisible(False)
        self.ui.tableWidget_3.horizontalHeader().setVisible(False) 
        for col in range(self.N):
            item = QTableWidgetItem(str(self.finalVect[col]))
            self.ui.tableWidget_3.setItem(0, col, item)
            self.ui.tableWidget_3.setColumnWidth(col, int(350/(self.N)))
        
    def ShowFinalErrors(self):
        self.ui.tableWidget_4.setColumnCount(self.N)
        self.ui.tableWidget_4.setRowCount(1)
        self.ui.tableWidget_4.verticalHeader().setVisible(False)
        self.ui.tableWidget_4.horizontalHeader().setVisible(False) 
        for col in range(self.N):
            item = QTableWidgetItem(str(self.error[col]))
            self.ui.tableWidget_4.setItem(0, col, item)
            self.ui.tableWidget_4.setColumnWidth(col, int(350/(self.N)))

    def show_warning_messagebox(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Wrong Input")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = msg.exec_()


    
    def Linear():
        window = LinearMatrix()
        window.show()

    if __name__ == '__main__':
        Linear()