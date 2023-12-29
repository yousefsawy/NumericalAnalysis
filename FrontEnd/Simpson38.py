import numpy as np
from scipy.integrate import quad
import math
import sys
from cmath import nan
import sympy as sp
# Add the path to the parent directory
import os
# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(current_dir)
# sys.path.append(parent_dir)
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
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
        func = f
        f = sp.lambdify('x', f, 'numpy')
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

        # Check if all y values are valid
        if counter == self.table.columnCount() - 1:
            try:
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
        # add image
        
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

    def show_function_page(self):
        self.stacked_widget.setCurrentWidget(self.function_page)

    def show_points_page(self):
        self.stacked_widget.setCurrentWidget(self.points_page)

    def show_about_page(self):
        self.stacked_widget.setCurrentWidget(self.about_page)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = Simpson38Form()
    main_app.show()
    sys.exit(app.exec_())