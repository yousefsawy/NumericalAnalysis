from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from Home import Ui_MainWindow
from mplwidget import MplWidget
import math
from CurveFittingMainWindow import Ui_CurveFittingForm
from Simpsons13MainWindow import Ui_Simpsons13
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.OpenHome()

        self.canvas = self.ui.widget.canvas
        self.figure = self.canvas.figure


        self.ui.pushButton_42.clicked.connect(self.VerifyFunc)
        self.ui.pushButton_2.clicked.connect(self.openCurveFitting)
        self.ui.pushButton_6.clicked.connect(self.openSimpsons13)

    def VerifyFunc(self):

        start = self.ui.textEdit_3.toPlainText()
        try:
            start = int(start)
        except:
            self.show_warning_messagebox('Start should be an integer')
            return


        func = self.ui.textEdit.toPlainText()
        try:
            func = convert_to_function(func)
            func(start)
        except:
            self.show_warning_messagebox('Function is incorrect')
            return

        stop = self.ui.textEdit_4.toPlainText()
        try:
            stop = int(stop)
        except:
            self.show_warning_messagebox('Stop should be an integer')
            return

        step = self.ui.textEdit_5.toPlainText()
        try:
            step = int(step)
        except:
            self.show_warning_messagebox('Step should be an integer')
            return

        self.plot_data(func,start,stop,step)





    def OpenHome(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def openCurveFitting(self):
        self.CurveFittingWindow = QtWidgets.QMainWindow()
        self.CurveFittingUI = Ui_CurveFittingForm()
        self.CurveFittingUI.setupUi(self.CurveFittingWindow)
        self.CurveFittingWindow.show()

    def openSimpsons13(self):
        self.Simpsons13Window = QtWidgets.QMainWindow()
        self.Simpsons13UI = Ui_Simpsons13()
        self.Simpsons13UI.setupUi(self.Simpsons13Window)
        self.Simpsons13Window.show()

    def show_warning_messagebox(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        msg.setText(message)

        msg.setWindowTitle("Wrong Input")

        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        retval = msg.exec_()

    def plot_data(self,func,start,end,step):
        # Generate sample data
        y = []
        x = []
        for i in range(start, end, step):
                y.append(func(i))
                x.append(i)

        self.figure.clear()

        ax = self.figure.add_subplot(111)
        ax.plot(x, y)

        self.canvas.draw()



def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()



def convert_to_function(input_string):
    # Replace sin, cos, ln, exp with math.sin, math.cos, math.log, math.exp respectively
    input_string = input_string.replace('sin', 'math.sin')
    input_string = input_string.replace('cos', 'math.cos')
    input_string = input_string.replace('ln', 'math.log')
    input_string = input_string.replace('exp', 'math.exp')

    # Evaluate the input string as a function
    def func(x):
        return eval(input_string)

    return func


if __name__ == "__main__":
    main()