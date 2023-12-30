from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget
import sys
import ast
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui_design import Ui_Widget   # Import the class generated from the UI file
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import romberg as r
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap  # Import QImage and QPixmap from PyQt5.QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt  # Import matplotlib.pyplot

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


from mplwidget import MplWidget
import math


import math

import math

import math

import math


def plot_data(canvas, func, start, end, step):
    # Generate sample data
    y = []
    x = []
    for i in range(start, end, step):
        y.append(func(i))
        x.append(i)

    canvas.figure.clear()
    ax = canvas.figure.add_subplot(111)
    ax.plot(x, y)
    canvas.draw()

def convert_to_function_x(input_string):
    # Replace sin, cos, ln, exp with np.sin, np.cos, np.log, np.exp respectively
    input_string = input_string.replace('sin', 'np.sin')
    input_string = input_string.replace('cos', 'np.cos')
    input_string = input_string.replace('ln', 'np.log')
    input_string = input_string.replace('exp', 'np.exp')
    input_string = input_string.replace('power', 'np.power')

    # Create a lambda function with one argument (x)

    func = lambda x: eval(input_string.replace('x', str(x)))

    return func
def convert_to_function(input_string):
    # Replace sin, cos, ln, exp with math.sin, math.cos, math.log, math.exp respectively
    input_string = input_string.replace('sin', 'math.sin')
    input_string = input_string.replace('cos', 'math.cos')
    input_string = input_string.replace('ln', 'math.log')
    input_string = input_string.replace('exp', 'math.exp')
    input_string = input_string.replace('power', 'math.pow')

    # Create a lambda function with two arguments (x and y)
    func = lambda x, y=None: eval(input_string.replace('x', str(x)).replace('y', 'None' if y is None else str(y)))

    return func


class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)
        self.setParent(parent)

class MyApp(QMainWindow, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.central_widget = None
        self.ok.clicked.connect(self.calculate_table)

    def calculate(self):
        lower_limit = int(self.lineEdit.text())
        upper_limit = int(self.lineEdit_2.text())
        exactvalue =int(self.lineEdit_6.text())
        order = int(self.lineEdit_3.text())
        step = int(self.lineEdit_5.text())
        fun = convert_to_function_x(self.lineEdit_4.text())
        res = r.Romberg_function(lower_limit, upper_limit, order, fun)
        self.textBrowser_3.setText(r.About_Section())
        self.textBrowser.setText(str(res))
        self.textBrowser_2.setText(r.True_Error(exactvalue,res))
        lower_limit_text = self.lineEdit.text()
        upper_limit_text = self.lineEdit_2.text()
        step_text = self.lineEdit_5.text()

        if not lower_limit_text or not upper_limit_text or not step_text:
            # Show a message or handle the case when any of the inputs is empty
            return
        fun = convert_to_function_x(self.lineEdit_4.text())

        # Create the MatplotlibCanvas instance if not already created
        if self.central_widget is None:
            self.central_widget = MatplotlibCanvas(self)
            self.setCentralWidget(self.central_widget)

        # Plot the data
        plot_data(self.central_widget, fun, lower_limit, upper_limit, step)

    def calculate_table(self):
        order = int(self.lineEdit_3.text())
        fun = convert_to_function(self.lineEdit_4.text())
        table = ast.literal_eval(self.textEdit.toPlainText())
        exactvalue =int(self.lineEdit_6.text())
        first_number = min(table.keys())
        last_number = max(table.keys())
        res = r.Romberg_func_table(table, fun, order)
        self.textBrowser_3.setText(r.About_Section())
        self.textBrowser.setText(str(res))
        step = int(self.lineEdit_5.text())
        self.textBrowser_2.setText(r.True_Error(exactvalue,res))
    def plot_function(self):
        lower_limit_text = self.lineEdit.text()
        upper_limit_text = self.lineEdit_2.text()
        step_text = self.lineEdit_5.text()

        if not lower_limit_text or not upper_limit_text or not step_text:
            # Show a message or handle the case when any of the inputs is empty
            return

        lower_limit = int(lower_limit_text)
        upper_limit = int(upper_limit_text)
        step = int(step_text)

        fun = convert_to_function_x(self.lineEdit_4.text())

        # Create the MatplotlibCanvas instance if not already created
        if self.central_widget is None:
            self.central_widget = MatplotlibCanvas(self)
            self.setCentralWidget(self.central_widget)

        # Plot the data
        plot_data(self.central_widget, fun, lower_limit, upper_limit, step)

def main():
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    app.exec_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
