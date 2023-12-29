import numpy as np
from scipy.integrate import quad
import math
import sys
from cmath import nan
import sympy as sp
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QScrollArea
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QTextEdit
from PyQt5.QtWidgets import  QHBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton, QTabWidget

def str2func(func):
    # Transforms the string to a mathematical function
    func = sp.sympify(func)
    # Return a lambda function that evaluates the sympy function
    return func

def get_delta(data):
    return [data[i + 1] - data[i] for i in range(len(data) - 1)]

def get_error(a, b, Ys):
    delta = Ys
    if len(Ys) < 5:
        return 0
    else:
        for i in range(4):
            delta = get_delta(delta)

    sum_delta4 = sum(delta)
    error = ((sum_delta4 / len(delta)) * (b - a)) / 6480
    return error*-1

def simpsons_3_8_rule(f, a, b, n, mode):
    func = f
    if mode ==1:
        f = sp.lambdify('x', f, 'numpy')

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    integral = y[0] + y[-1]
    for i in range(1, n):
        if i % 3 == 1:
            integral += 3 * y[i]
        elif i % 3 == 2:
            integral += 3 * y[i]
        else:
            integral += 2 * y[i]

    integral *= (3 * h / 8)

    if mode == 1:
        z = sp.symbols('x')
        third_derivative = sp.diff(func, z, 3)
        fourth_derivative = (third_derivative.subs(z, x[-1]) - third_derivative.subs(z, x[0])) / (x[-1] - x[0])
        error = ((x[-1] - x[0]) ** 5 * fourth_derivative) / (
                    6840 * n **4)  # Error calculation using scipy's quad function
    else:
        error = get_error(a, b, y)

    return integral, error

def show_alert(message):
        alert = QMessageBox()
        alert.setIcon(QMessageBox.Warning)
        alert.setText(message)
        alert.setWindowTitle("Input Validation Error")
        alert.exec_()

class PointsPage(QWidget):
    def __init__(self):
        super(PointsPage, self).__init__()

        # Create widgets
        self.lower_bound_label = QLabel("Lower Bound:")
        self.lower_bound_input = QLineEdit(self) #a

        self.upper_bound_label = QLabel("Upper Bound:")
        self.upper_bound_input = QLineEdit(self) #b

        self.intervals_label = QLabel("Intervals:")
        self.intervals_input = QLineEdit(self) #n

        self.show_table_button = QPushButton("Show Table", self) #check and show alert
        self.table = QTableWidget(self) 

        #insert calculation of result and error
        self.show_result_button = QPushButton("Show Result", self) 
        self.result_label = QLabel("Result:")
        self.error_label = QLabel("Error:")

        # Store y values in an array
        #self.y_values = []

        # Set up layout
        layout = QVBoxLayout(self)

        input_layout = QHBoxLayout()
        
        input_layout.addWidget(self.lower_bound_label)
        input_layout.addWidget(self.lower_bound_input)
        input_layout.addWidget(self.upper_bound_label)
        input_layout.addWidget(self.upper_bound_input)
        input_layout.addWidget(self.intervals_label)
        input_layout.addWidget(self.intervals_input)
        input_layout.addWidget(self.show_table_button)

        layout.addLayout(input_layout)
        layout.addWidget(self.table)
        layout.addWidget(self.show_result_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.error_label)
        
        # Connect button click events to slots
        self.show_table_button.clicked.connect(self.show_table)
        self.show_result_button.clicked.connect(self.show_result)

    def show_table(self):
        # Get values from input boxes
        lower_bound = self.lower_bound_input.text()
        upper_bound = self.upper_bound_input.text()
        intervals = self.intervals_input.text()

        # Validate lower_bound and upper_bound
        try:
            a = float(lower_bound)
            b = float(upper_bound)
            if not lower_bound or not upper_bound or lower_bound==upper_bound:
                raise ValueError
        except ValueError:
            show_alert("Please enter a valid number for lower and upper bounds.")
            return

        # Validate intervals
        try:
            n = int(intervals) 
            if not intervals or n <= 0 or n != int(intervals) or  n % 3 != 0 :
                raise ValueError
        except ValueError:
            show_alert("Please enter a valid whole positive number that is divisible by 3 for intervals.")
            return
            
        # Calculate x values based on the given bounds and intervals
        x_values = [round(a + i * ((b - a) / n), 2) for i in range(n + 1)]

        # Set up the table
        self.table.setRowCount(2)
        self.table.setColumnCount(n + 2)
        # Hide the horizontal header
        self.table.horizontalHeader().setVisible(False)

        # Fill the x row with 'x' in the first column
        item_x = QTableWidgetItem('x')
        self.table.setItem(0, 0, item_x)
        # Fill the x row
        for i in range(n + 1):
            item = QTableWidgetItem(str(x_values[i]))
            self.table.setItem(0, i+1, item)
        # Fill the y row with 'y' in the first column
        item_y = QTableWidgetItem('y')
        self.table.setItem(1, 0, item_y)

    def show_result(self):
        # Validate that all y values are numbers and not empty
        points = []
        counter = 0
        for i in range(1, self.table.columnCount()):
            point = []
            item_y = self.table.item(1, i)
            item_x = self.table.item(0, i)
            if not item_y or not item_y.text().strip():
                show_alert("Please enter valid numbers for all y values.")
                return
            try:
                y_value = float(item_y.text())
                x_value = float(item_x.text())
                # point.append(x_value)
                # point.append(y_value)
                point = [x_value,y_value]
                points.append(point)
                counter = counter +1
            except ValueError:
                show_alert("Please enter valid numbers for all y values.")
                return
            
            print("points:" , points)

        ##########################################
        equidistant = 0
        x1=self.table.item(0, 1)
        x2=self.table.item(0, 2)
        common_difference = float(x2.text()) - float(x1.text())
        for i in range(3, self.table.columnCount()):
            x1=self.table.item(0, i-1)
            x2=self.table.item(0, i)
            if (float(x2.text()) - float(x1.text())) != common_difference:
                equidistant = equidistant + 1
        ###########################################
                
        # Check if all y values are valid
        if counter == self.table.columnCount() - 1:
            try:
                if equidistant!=0:
                    show_alert("Error during calculations since the points are no longer equidistant.")
                    return
                
                a = float(self.lower_bound_input.text())
                b = float(self.upper_bound_input.text())
                n = int(self.intervals_input.text())
                
                Points = np.array(points)
                #print(x_values,y_values)

                result, error = simpsons_3_8_rule(lambda x: np.interp(x, Points[:, 0], Points[:, 1]), a, b, n, 0)
                # Display the result and error
                self.result_label.setText(f"Result: {result}")
                self.error_label.setText(f"Error: {error}")
            except Exception as e:
                show_alert("Error during calculations.")
                print (e)
                return
        else:
            show_alert("Please enter valid numbers for all y values.")
            # Placeholder for your result calculation
            result = "Result: N/A"
            error = "Error: N/A"
            # Display the result and error
            self.result_label.setText(result)
            self.error_label.setText(error)

class AboutPage(QWidget):
    def __init__(self):
        super(AboutPage, self).__init__()
        self.image_label = QLabel(self)
        
        # Get the absolute path to the script's directory
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Load the image using an absolute path
        image_path = os.path.join(script_dir, "About_Simpson382.jpg")
        pixmap = QPixmap(image_path)

        if pixmap.isNull():
            print(f"Error loading image from: {image_path}")
        else:
            self.image_label.setPixmap(pixmap)

       # Set up the page layout
        # layout = QVBoxLayout(self)
        # layout.addWidget(self.image_label)

        # Create a scroll area and set the image label as its widget
        scroll_area = QScrollArea(self)
        scroll_area.setWidget(self.image_label)
        scroll_area.setWidgetResizable(True)

        # Set the layout of the scroll area
        scroll_area_layout = QVBoxLayout(self)
        scroll_area_layout.addWidget(scroll_area)
        
class FunctionPage(QWidget):
    def __init__(self):
        super(FunctionPage, self).__init__()

        # Create widgets
        self.function_label = QLabel("Function: (the dependent variable is x)")
        self.function_input = QLineEdit(self)

        self.lower_bound_label = QLabel("Lower Bound:")
        self.lower_bound_input = QLineEdit(self)

        self.upper_bound_label = QLabel("Upper Bound:")
        self.upper_bound_input = QLineEdit(self)

        self.intervals_label = QLabel("Intervals:")
        self.intervals_input = QLineEdit(self)

        self.calculate_button = QPushButton("Calculate", self)
        self.result_label = QLabel("Result:")
        self.error_label = QLabel("Error:")

        # Set up layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.function_label)
        layout.addWidget(self.function_input)
        layout.addWidget(self.lower_bound_label)
        layout.addWidget(self.lower_bound_input)
        layout.addWidget(self.upper_bound_label)
        layout.addWidget(self.upper_bound_input)
        layout.addWidget(self.intervals_label)
        layout.addWidget(self.intervals_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.error_label)

        # Connect the button click event to a calculation method
        self.calculate_button.clicked.connect(self.calculate_result)

    def calculate_result(self):

        # Get values from input boxes
        function_str = self.function_input.text()
        lower_bound = self.lower_bound_input.text()
        upper_bound = self.upper_bound_input.text()
        intervals = self.intervals_input.text()

        # Validate lower_bound and upper_bound
        try:
            a = float(lower_bound)
            b = float(upper_bound)
            if not lower_bound or not upper_bound or lower_bound==upper_bound:
                raise ValueError
        except ValueError:
            show_alert("Please enter a valid number for lower and upper bounds.")
            return

        # Validate intervals
        try:
            n = int(intervals)
            if not intervals or n <= 0 or n != int(intervals):
                raise ValueError
        except ValueError:
            show_alert("Please enter a valid whole positive number for intervals.")
            return
        
        # Validate function
        if not function_str:
            show_alert("Empty Function.")
            return
        else:
            func = str2func(function_str)
            try:
                result,error = simpsons_3_8_rule(func, a, b, n, 1)
                if result == float('inf') or result == float('-inf'):
                    show_alert("Numerical integration failed, because the integral is divergent.")
                else:
                    # Display the result
                    self.result_label.setText(f"Result: {result}")
                    self.error_label.setText(f"Error: {error}") 
            except Exception:
                show_alert("Incorrect function, you either entered an undefined function or used multiple variables.")

class Simpson38Form(QMainWindow):
    def __init__(self):
        super(Simpson38Form, self).__init__()

        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # Create and add the pages to the tab widget
        self.function_page = FunctionPage()
        self.points_page = PointsPage()
        self.about_page = AboutPage()

        self.tab_widget.addTab(self.function_page, "Function")
        self.tab_widget.addTab(self.points_page, "Points")
        self.tab_widget.addTab(self.about_page, "About")

        # Show the default tab
        self.tab_widget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyleSheet("""
        /*
Material Dark Style Sheet for QT Applications
Author: Jaime A. Quiroga P.
Inspired on https://github.com/jxfwinter/qt-material-stylesheet
Company: GTRONICK
Last updated: 04/12/2018, 15:00.
Available at: https://github.com/GTRONICK/QSS/blob/master/MaterialDark.qss
*/
QMainWindow {
	background-color:#1e1d23;
}
QDialog {
	background-color:#1e1d23;
}
QColorDialog {
	background-color:#1e1d23;
}
QTextEdit {
	background-color:#1e1d23;
	color: #a9b7c6;
}
QPlainTextEdit {
	selection-background-color:#007b50;
	background-color:#1e1d23;
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-width: 1px;
	color: #a9b7c6;
}

QToolButton {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #04b97f;
	border-bottom-width: 1px;
	border-style: solid;
	color: #a9b7c6;
	padding: 2px;
	background-color: #1e1d23;
}
QToolButton:hover{
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #37efba;
	border-bottom-width: 2px;
	border-style: solid;
	color: #FFFFFF;
	padding-bottom: 1px;
	background-color: #1e1d23;
}

QLineEdit {
	border-width: 1px; border-radius: 4px;
	border-color: rgb(58, 58, 58);
	border-style: inset;
	padding: 0 8px;
	color: #a9b7c6;
	background:#1e1d23;
	selection-background-color:#007b50;
	selection-color: #FFFFFF;
}
QLabel {
	color: #a9b7c6;
}
QLCDNumber {
	color: #37e6b4;
}
QProgressBar {
	text-align: center;
	color: rgb(240, 240, 240);
	border-width: 1px; 
	border-radius: 10px;
	border-color: rgb(58, 58, 58);
	border-style: inset;
	background-color:#1e1d23;
}
QProgressBar::chunk {
	background-color: #04b97f;
	border-radius: 5px;
}
QMenuBar {
	background-color: #1e1d23;
}
QMenuBar::item {
	color: #a9b7c6;
  	spacing: 3px;
  	padding: 1px 4px;
  	background: #1e1d23;
}

QMenuBar::item:selected {
  	background:#1e1d23;
	color: #FFFFFF;
}
QMenu::item:selected {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: #04b97f;
	border-bottom-color: transparent;
	border-left-width: 2px;
	color: #FFFFFF;
	padding-left:15px;
	padding-top:4px;
	padding-bottom:4px;
	padding-right:7px;
	background-color: #1e1d23;
}
QMenu::item {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-bottom-width: 1px;
	border-style: solid;
	color: #a9b7c6;
	padding-left:17px;
	padding-top:4px;
	padding-bottom:4px;
	padding-right:7px;
	background-color: #1e1d23;
}
QMenu{
	background-color:#1e1d23;
}
QTabWidget {
	color:rgb(0,0,0);
	background-color:#1e1d23;
}
QTabWidget::pane {
		border-color: rgb(77,77,77);
		background-color:#1e1d23;
		border-style: solid;
		border-width: 1px;
    	border-radius: 6px;
}
QTabBar::tab {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-bottom-width: 1px;
	border-style: solid;
	color: #808086;
	padding: 3px;
	margin-left:3px;
	background-color: #1e1d23;
}
QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {
  	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #04b97f;
	border-bottom-width: 2px;
	border-style: solid;
	color: #FFFFFF;
	padding-left: 3px;
	padding-bottom: 2px;
	margin-left:3px;
	background-color: #1e1d23;
}

QCheckBox {
	color: #a9b7c6;
	padding: 2px;
}
QCheckBox:disabled {
	color: #808086;
	padding: 2px;
}

QCheckBox:hover {
	border-radius:4px;
	border-style:solid;
	padding-left: 1px;
	padding-right: 1px;
	padding-bottom: 1px;
	padding-top: 1px;
	border-width:1px;
	border-color: rgb(87, 97, 106);
	background-color:#1e1d23;
}
QCheckBox::indicator:checked {

	height: 10px;
	width: 10px;
	border-style:solid;
	border-width: 1px;
	border-color: #04b97f;
	color: #a9b7c6;
	background-color: #04b97f;
}
QCheckBox::indicator:unchecked {

	height: 10px;
	width: 10px;
	border-style:solid;
	border-width: 1px;
	border-color: #04b97f;
	color: #a9b7c6;
	background-color: transparent;
}
QRadioButton {
	color: #a9b7c6;
	background-color: #1e1d23;
	padding: 1px;
}
QRadioButton::indicator:checked {
	height: 10px;
	width: 10px;
	border-style:solid;
	border-radius:5px;
	border-width: 1px;
	border-color: #04b97f;
	color: #a9b7c6;
	background-color: #04b97f;
}
QRadioButton::indicator:!checked {
	height: 10px;
	width: 10px;
	border-style:solid;
	border-radius:5px;
	border-width: 1px;
	border-color: #04b97f;
	color: #a9b7c6;
	background-color: transparent;
}
QStatusBar {
	color:#027f7f;
}
QSpinBox {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QDoubleSpinBox {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QTimeEdit {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QDateTimeEdit {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QDateEdit {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QComboBox {
	color: #a9b7c6;	
	background: #1e1d23;
}
QComboBox:editable {
	background: #1e1d23;
	color: #a9b7c6;
	selection-background-color: #1e1d23;
}
QComboBox QAbstractItemView {
	color: #a9b7c6;	
	background: #1e1d23;
	selection-color: #FFFFFF;
	selection-background-color: #1e1d23;
}
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
	color: #a9b7c6;	
	background: #1e1d23;
}
QFontComboBox {
	color: #a9b7c6;	
	background-color: #1e1d23;
}
QToolBox {
	color: #a9b7c6;
	background-color: #1e1d23;
}
QToolBox::tab {
	color: #a9b7c6;
	background-color: #1e1d23;
}
QToolBox::tab:selected {
	color: #FFFFFF;
	background-color: #1e1d23;
}
QScrollArea {
	color: #FFFFFF;
	background-color: #1e1d23;
}
QSlider::groove:horizontal {
	height: 5px;
	background: #04b97f;
}
QSlider::groove:vertical {
	width: 5px;
	background: #04b97f;
}
QSlider::handle:horizontal {
	background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
	border: 1px solid #5c5c5c;
	width: 14px;
	margin: -5px 0;
	border-radius: 7px;
}
QSlider::handle:vertical {
	background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);
	border: 1px solid #5c5c5c;
	height: 14px;
	margin: 0 -5px;
	border-radius: 7px;
}
QSlider::add-page:horizontal {
    background: white;
}
QSlider::add-page:vertical {
    background: white;
}
QSlider::sub-page:horizontal {
    background: #04b97f;
}
QSlider::sub-page:vertical {
    background: #04b97f;
}
/*split*/
QPushButton{
	border-style: solid;
	border-color: #050a0e;
	border-width: 1px;
	border-radius: 5px;
	color: #d3dae3;
	padding: 2px;
	background-color: #100E19;
}
QPushButton::default{
	border-style: solid;
	border-color: #050a0e;
	border-width: 1px;
	border-radius: 5px;
	color: #FFFFFF;
	padding: 2px;
	background-color: #151a1e;
}
QPushButton:hover{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);
    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);
    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);
    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);
	border-width: 2px;
    border-radius: 1px;
	color: #d3dae3;
	padding: 2px;
}
QPushButton:pressed{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);
    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);
    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);
    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);
	border-width: 2px;
    border-radius: 1px;
	color: #d3dae3;
	padding: 2px;
}

QStackedWidget {
    background-color: #1e1d23;
    border: 1px solid rgb(77, 77, 77);
    border-radius: 6px;
}

QStackedWidget {
    background-color: #1e1d23;
    border: 1px solid rgb(77, 77, 77);
    border-radius: 6px;
}

QStackedWidget::widget {
    padding: 6px;
}

QStackedWidget::widget:selected {
    background-color: #1e1d23;
    border-bottom: 2px solid #04b97f;
}

QStackedWidget::widget:hover {
    border-bottom: 1px solid #04b97f;
}

    """)

    main_app = Simpson38Form()
    main_app.show()
    sys.exit(app.exec_())