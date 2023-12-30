import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from eigenvalue import Ui_MainWindow
from eigen_logic import maxeigen, mineigen, max_deflation_matrix, min_deflation_matrix, secondmax, secondmin

class Eigen(QMainWindow):

    def __init__(self):
        super().__init__()
        self.OpenEigen()
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton.clicked.connect(self.initInput)
        self.ui.pushButton.clicked.connect(self.executeFunc)
                
    def OpenEigen(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def initInput(self):
        self.ValidateInputN()
        self.initInputMatrix()
        self.initInputVector()

    def ValidateInputN(self):
        try:
            self.N = int(self.ui.lineEdit_2.text())
            if (self.N<1):
                raise Exception("N should be a positive integer")
        except:
            self.show_warning_messagebox('N should be an integer')
            return
        
    def initInputMatrix(self):
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.horizontalHeader().setVisible(False)  
        self.InitRowsAndColumns()

    def InitRowsAndColumns(self):
        self.ui.tableWidget.setColumnCount(self.N)
        self.ui.tableWidget.setRowCount(self.N)
        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                item = QTableWidgetItem('')
                self.ui.tableWidget.setItem(row, col, item)
            self.ui.tableWidget.setRowHeight(row,int(160/self.N))
        
        for col in range(self.ui.tableWidget.columnCount()):
            self.ui.tableWidget.setColumnWidth(col, int(320 / (self.N + 1)))
        
    def initInputVector(self):
        self.ui.tableWidget_2.setRowCount(self.N)
        self.ui.tableWidget_2.setColumnCount(1)
        self.ui.tableWidget_2.verticalHeader().setVisible(False)
        self.ui.tableWidget_2.horizontalHeader().setVisible(False) 
        for row in range(self.ui.tableWidget_2.rowCount()):
            item = QTableWidgetItem('')
            self.ui.tableWidget_2.setItem(row,0, item)
            self.ui.tableWidget_2.setColumnWidth(row, 40)
            self.ui.tableWidget_2.setRowHeight(row, int(160/self.N))
    
    def ValidateMatrixInputs(self):
        self.matrix = []
        try:
            for row in range(self.N):
                OneRow = []
                for col in range(self.N):
                    OneRow.append(float(self.ui.tableWidget.item(row, col).text()))
                self.matrix.append(OneRow)
        except:
            self.show_warning_messagebox('Invalid Matrix Input')
            return
        
    def ValidateVectorInputs(self):
        self.vector = [0]*self.N
        try:
            for col in range(self.N):
                self.vector[col]=(float(self.ui.tableWidget_2.item(0, col).text()))
        except:
            self.show_warning_messagebox('Invalid Vector Input')
            return
    
    def ValidateIterations(self):
        try:
            self.iterations = int(self.ui.lineEdit_3.text())
            if (self.iterations<1):
                raise Exception("Iterations No. should be a positive integer")
        except:
            self.show_warning_messagebox('iterations number should be an integer')
            return

    def ValidateInput(self):
        self.ValidateMatrixInputs()
        self.ValidateVectorInputs()
        self.ValidateIterations()


    def executeFunc(self):
        self.ValidateInput()
        if (self.defMatrix!=[]):
            self.ShowFinalMatrix()
        self.ShowLamda()
        self.ShowVector()


    def ChooseFunc(self):
        if (self.ui.radio_button_1.isChecked()==True):
            self.eigen= maxeigen(self.matrix, self.vector, self.iterations)
        if (self.ui.radio_button_2.isChecked()==True):
            self.eigen= mineigen(self.matrix, self.vector, self.iterations)
        if (self.ui.radio_button_3.isChecked()==True):
            self.eigen= maxeigen(self.matrix, self.vector, self.iterations)
            lamda_max, x = self.eigen
            self.defMatrix = max_deflation_matrix(self.matrix, self.vector, lamda_max)
        if (self.ui.radio_button_4.isChecked()==True):
            self.eigen= mineigen(self.matrix, self.vector, self.iterations)
            lamda_max, x = self.eigen
            self.defMatrix = min_deflation_matrix(self.matrix, self.vector, lamda_min)
        if (self.ui.radio_button_5.isChecked()==True):
            lamda_max, x= maxeigen(self.matrix, self.vector, self.iterations)
            self.defMatrix= max_deflation_matrix(self.matrix, self.vector, lamda_max)
            self.eigen = secondmax(self.defMatrix, self.vector, self.iterations)
        if (self.ui.radio_button_6.isChecked()==True):
            lamda_min, x= mineigen(self.matrix, self.vector, self.iterations)
            self.defMatrix= min_deflation_matrix(self.matrix, self.vector, lamda_min)
            self.eigen = secondmin(self.defMatrix, self.vector, self.iterations)

        

    def ShowFinalMatrix(self):
        self.ui.tableWidget_3.setColumnCount(self.N)
        self.ui.tableWidget_3.setRowCount(self.N)
        self.ui.tableWidget_3.verticalHeader().setVisible(False)
        self.ui.tableWidget_3.horizontalHeader().setVisible(False)
        for row in range(self.N):
            for col in range(self.N):
                item = QTableWidgetItem(str(self.defMatrix[row][col]))
                self.ui.tableWidget_3.setItem(row, col, item)
                self.ui.tableWidget_3.setColumnWidth(col, int(170/(self.N)))
            self.ui.tableWidget_3.setRowHeight(row, int(90/(self.N)))

    def ShowVector(self):
        self.ui.tableWidget_4.setColumnCount(1)
        self.ui.tableWidget_4.setRowCount(self.N)
        self.ui.tableWidget_4.verticalHeader().setVisible(False)
        self.ui.tableWidget_4.horizontalHeader().setVisible(False) 
        for row in range(self.N):
            item = QTableWidgetItem(str(self.eigen[1][row]))
            self.ui.tableWidget_4.setItem(row, 0, item)
            self.ui.tableWidget_4.setColumnWidth(51)
        self.ui.tableWidget_3.setRowHeight(row, int(120/(self.N)))

    def ShowLamda(self):
        self.ui.textBrowser.setText(str(self.eigen[0]))

    def show_warning_messagebox(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Wrong Input")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = msg.exec_()


    
def Linear():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    Linear()