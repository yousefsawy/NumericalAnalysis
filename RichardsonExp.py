from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from RichardsonExpUi import Ui_RichardsonExp
from mplwidget import MplWidget
import math

class RichardsonExp_Control(QMainWindow):
    def __init__(self):
        super().__init__()

        self.rich_window = QtWidgets.QMainWindow()
        self.rich_ui = Ui_RichardsonExp()
        self.rich_ui.setupUi(self.rich_window)

        self.canvas = self.rich_ui.widget.canvas
        self.figure = self.canvas.figure
        self.rich_ui.pushButton_2.clicked.connect(self.Graph)
        self.rich_ui.pushButton.clicked.connect(self.Solve)



    def OpenRich(self):
        self.rich_window.show()

    def Solve(self):

        #Derivative Order

        drvorder = self.rich_ui.textEdit_2.toPlainText()
        try:
            drvorder = float(drvorder)
        except:
            self.show_warning_messagebox('Derivative order should be an integer')
            return

        if drvorder != 1 and drvorder != 2:
            self.show_warning_messagebox('Derivative Order should be 1 or 2')

        #X
        x = self.rich_ui.textEdit_3.toPlainText()
        try:
            x = float(x)
        except:
            self.show_warning_messagebox('X should be an integer')
            return

        #Function
        func = self.rich_ui.textEdit.toPlainText()
        try:
            func = convert_to_function(func)
            func(x)
        except:
            self.show_warning_messagebox('Function is incorrect')
            return

        #Max Step
        max_step = self.rich_ui.textEdit_4.toPlainText()
        try:
            max_step = float(max_step)
        except:
            self.show_warning_messagebox('Step should be an integer')
            return

        #Order
        order = self.rich_ui.textEdit_5.toPlainText()
        try:
            order = float(order)
        except:
            self.show_warning_messagebox('order should be an integer')
            return

        if order != 2 and order != 4 and order != 6 and order != 8:
            self.show_warning_messagebox('order should be 2 for O(h^2) / 4 for O(h^4) / 6 for O(h^6) / 8 for O(h^8)')

        self.rich_ui.label_12.setText(str(richardson_extrapolator(func,drvorder,x,max_step,order)))

    def Graph(self):

        #Derivative Order

        drvorder = self.rich_ui.textEdit_2.toPlainText()
        try:
            drvorder = float(drvorder)
        except:
            self.show_warning_messagebox('Derivative order should be an integer')
            return

        if drvorder != 1 and drvorder != 2:
            self.show_warning_messagebox('Derivative Order should be 1 or 2')

        #X
        x = self.rich_ui.textEdit_3.toPlainText()
        try:
            x = float(x)
        except:
            self.show_warning_messagebox('X should be an integer')
            return

        #Function
        func = self.rich_ui.textEdit.toPlainText()
        try:
            func = convert_to_function(func)
            func(x)
        except:
            self.show_warning_messagebox('Function is incorrect')
            return

        #Max Step
        max_step = self.rich_ui.textEdit_4.toPlainText()
        try:
            max_step = float(max_step)
        except:
            self.show_warning_messagebox('Step should be an integer')
            return

        #Order
        order = self.rich_ui.textEdit_5.toPlainText()
        try:
            order = float(order)
        except:
            self.show_warning_messagebox('order should be an integer')
            return

        if order != 2 and order != 4 and order != 6 and order != 8:
            self.show_warning_messagebox('order should be 2 for O(h^2) / 4 for O(h^4) / 6 for O(h^6) / 8 for O(h^8)')

        def richFunc(x):
            return richardson_extrapolator(func, drvorder, x, max_step, order)


        start = self.rich_ui.textEdit_9.toPlainText()
        try:
            start = int(start)
        except:
            self.show_warning_messagebox('Start should be an integer')
            return


        stop = self.rich_ui.textEdit_10.toPlainText()
        try:
            stop = int(stop)
        except:
            self.show_warning_messagebox('Stop should be an integer')
            return

        step = self.rich_ui.textEdit_8.toPlainText()
        try:
            step = int(step)
        except:
            self.show_warning_messagebox('Step should be an integer')
            return


        self.plot_data(richFunc,start,stop,step)

    def show_warning_messagebox(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        msg.setText(message)

        msg.setWindowTitle("Wrong Input")

        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        retval = msg.exec_()

    def mate2refneesh(self,x):
        return x

    def plottest(self):
        self.plot_data(self.mate2refneesh,-5,5,1)
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

def richardson_extrapolator(function, derivative_order, x, max_step,order):
  if derivative_order == 1:
    if order == 2:
      derivative = (function(x + max_step) - function(x - max_step)) / (2 * max_step)
      return derivative
    elif order == 4:
      h = [max_step, max_step / 2]
      table = []
      for i in range(2):
        ans = (function(x + h[i]) - function(x - h[i])) / (2 * h[i])
        table.append(ans)
      derivative = (4 * table[1] - table[0]) / 3
      return derivative
    elif order == 6:
      h = [max_step, max_step / 2, max_step / 4]
      table = []
      for i in range(3):
        ans = (function(x + h[i]) - function(x - h[i])) / (2 * h[i])
        table.append(ans)
      for i in range(2):
        table.append((4 * table[i + 1] - table[i]) / 3)
      derivative = (16 * table[4] - table[3]) / 15
      return derivative
    elif order == 8:
      h = [max_step, max_step / 2, max_step / 4, max_step / 8]
      table = []
      for i in range(4):
        ans = (function(x + h[i]) - function(x - h[i])) / (2 * h[i])
        table.append(ans)
      for i in range(3):
        table.append((4 * table[i + 1] - table[i]) / 3)
      for i in range(2):
        table.append((16 * table[i + 5] - table[i + 4]) / 15)
      derivative = (64 * table[8] - table[7]) / 63
      return derivative
  elif derivative_order == 2:
    if order == 2:
      derivative = (function(x + max_step) + function(x - max_step) - 2 * function(x)) / (max_step ** 2)
      return derivative
    elif order == 4:
      h = [max_step, max_step / 2]
      table = []
      for i in range(2):
        ans = (function(x + h[i]) + function(x - h[i]) - 2 * function(x)) / (h[i] ** 2)
        table.append(ans)
      derivative = (4 * table[1] - table[0]) / 3
      return derivative
    elif order == 6:
      h = [max_step, max_step / 2, max_step / 4]
      table = []
      for i in range(3):
        ans = (function(x + h[i]) + function(x - h[i]) - 2 * function(x)) / (h[i] ** 2)
        table.append(ans)
      for i in range(2):
        table.append((4 * table[i + 1] - table[i]) / 3)
      derivative = (16 * table[4] - table[3]) / 15
      return derivative
    elif order == 8:
      h = [max_step, max_step / 2, max_step / 4, max_step / 8]
      table = []
      for i in range(4):
        ans = (function(x + h[i]) + function(x - h[i]) - 2 * function(x)) / (h[i] ** 2)
        table.append(ans)
      for i in range(3):
        table.append((4 * table[i + 1] - table[i]) / 3)
      for i in range(2):
        table.append((16 * table[i + 5] - table[i + 4]) / 15)
      derivative = (64 * table[8] - table[7]) / 63
      return derivative