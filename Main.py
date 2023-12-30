from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from Home import Ui_MainWindow
from RichardsonExp import RichardsonExp_Control
from Predictor import Ui_Predictor
from DifferentialEqn import DifferentialEquationSolver
from Lagrange_with_graph import LagrangeInterpolationCalculator
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mplwidget import MplWidget
from RK import RK_UI
from LinearMatrix import Linear_UI
from Trapezoidal import TrapezoidalForm
from Simpson38 import Simpson38Form
from Eigen import EigenForm
import math
from Newton_Equi import Newton_Equi_Form
from newton_general import newton_general_Form

import math
from CurveFittingMainWindow import Ui_CurveFittingForm
from Simpsons13MainWindow import Ui_Simpsons13

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.trapezoidal_form = None
        self.simpson38_form = None

        self.NewtonGeneral_Form = None
        self.NewtonEqui_Form = None

        self.OpenHome()
        self.canvas = self.ui.widget.canvas
        self.figure = self.canvas.figure

        self.rich_control = RichardsonExp_Control()
        self.ui.pushButton_42.clicked.connect(self.VerifyFunc)
        self.ui.pushButton_12.clicked.connect(self.OpenRich)
        self.ui.pushButton_28.clicked.connect(self.OpenPredictor)
        self.ui.pushButton_4.clicked.connect(self.OpenLagrange)
        self.ui.pushButton_5.clicked.connect(self.OpenNewtonGenral)
        self.ui.pushButton_3.clicked.connect(self.OpenNewtonEqui)
        self.ui.pushButton_42.clicked.connect(self.VerifyFunc)
        self.ui.pushButton_24.clicked.connect(self.OpenLinear)
        self.ui.pushButton_27.clicked.connect(self.OpenRKMain)
        self.ui.pushButton_8.clicked.connect(self.OpenTrapezoidal)
        self.ui.pushButton_9.clicked.connect(self.OpenSimpson38)
        self.ui.pushButton_2.clicked.connect(self.openCurveFitting)
        self.ui.pushButton_6.clicked.connect(self.openSimpsons13)
        self.ui.pushButton_48.clicked.connect(self.openEigenProblem)
    
    def openEigenProblem(self):
        self.eigen_form = EigenForm()
        self.eigen_form.show()

    def OpenPredictor(self):
        self.predict_window = QtWidgets.QMainWindow()
        self.predict_Ui = Ui_Predictor()
        self.predict_Ui.setupUi(self.predict_window)
        self.predict_window.show()

    def OpenDiff(self):
        self.diff_window = DifferentialEquationSolver()
        self.diff_window.show()

    def OpenLagrange(self):
        self.Lagrange_window = LagrangeInterpolationCalculator()
        self.Lagrange_window.show()
        
    def OpenRich(self):
        self.rich_control.OpenRich()

    def OpenTrapezoidal(self):
        if not self.trapezoidal_form:
            self.trapezoidal_form = TrapezoidalForm()
        self.trapezoidal_form.show()

    def OpenSimpson38(self):
        if not self.simpson38_form:
            self.simpson38_form = Simpson38Form()
        self.simpson38_form.show()
        
    def OpenNewtonGenral(self):
        self.NewtonGeneralWindow = QtWidgets.QMainWindow()
        self.NewtonGeneralUI = newton_general_Form()
        self.NewtonGeneralUI.setupUi(self.NewtonGeneralWindow)
        self.NewtonGeneralWindow.show() 

    def OpenNewtonEqui(self):
        self.NewtonEquiWindow = QtWidgets.QMainWindow()
        self.NewtonEquiUI = Newton_Equi_Form()
        self.NewtonEquiUI.setupUi(self.NewtonEquiWindow)
        self.NewtonEquiWindow.show()      

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

    def OpenRKMain(self):
        self.RK_window = RK_UI()
        self.RK_window.show()

    def OpenLinear(self):
        self.Linear_window = Linear_UI()
        self.Linear_window.show()


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
