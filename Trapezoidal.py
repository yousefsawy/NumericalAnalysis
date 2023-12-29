import sys
from cmath import nan
import sympy as sp
# Add the path to the parent directory
# import os
# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(current_dir)
# sys.path.append(parent_dir)
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QTextEdit
from PyQt5.QtWidgets import  QHBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton, QTabWidget
#from MathSoln.Trapezoidal import TrapezoidalFunction, TrapezoidalTable

def str2func(func):

     # Transforms the string to a mathematical function
     func = sp.sympify(func)

     # Return a lambda function that evaluates the sympy function
     return lambda x: func.subs("x", x).evalf()

# Integrates using the trapezoidal method if given function
def TrapezoidalFunction(f,a,b,n):
    h = (b-a)/n
    summation = 0
    fa = f(a)
    x = sp.symbols('x')
    # Checks if any of them is either undefined or infinity then calculates the limit.
    if fa == sp.nan or fa == sp.zoo:
        fa = sp.limit(f(x), x, a)
    fb = f(b)
    if  fb == sp.nan or fb == sp.zoo:
        fb = sp.limit(f(x), x, b)
    for i in range(1, n):
        val = f(a + i * h)
        # Checks if it is either undefined or infinity then calculates the limit.
        if val == sp.nan or val == sp.zoo:
            val = sp.limit(f(x), x, a + i * h)
        summation += val
    return h/2*(fa + fb + 2*summation)

# Integrates using the trapezoidal method if given table
def TrapezoidalTable(h,y):
    n = len(y)
    summation = 0
    for i in range(0, n):
        if i == 0 or i == n-1:
            summation += y[i]
        else:
            summation += 2*y[i]
    return h/2 * summation

# Calculates finite difference for error if given function
def FiniteDiff(f,a,h):
    x = sp.symbols('x')
    fxmin = f(a-h)
    # Checks if any of them is either undefined or infinity then calculates the limit.
    if fxmin == sp.nan or fxmin == sp.zoo:
        fxmin = sp.limit(f(x),x,a-h)
    fxmax = f(a+h)
    if fxmax == sp.nan or fxmax == sp.zoo:
        fxmax = sp.limit(f(x),x,a+h)
    return (fxmax-fxmin)/(2*h)

# Calculates the error of the integration if given function
def TrapErrorFunction(f,a,b,h):
    finite = FiniteDiff(f,b,h) - FiniteDiff(f,a,h)
    return h**2/12 * finite

# Integrates using the trapezoidal method if given table
def TrapezoidalTable(h,y):
    n = len(y)
    summation = 0
    for i in range(0, n):
        if i == 0 or i == n-1:
            summation += y[i]
        else:
            summation += 2*y[i]
    return h/2 * summation

# Simple Difference Table
def DifferenceTable(y):
    n = len(y)
    out = []
    for i in range(0,n-1):
        out.append(y[i+1] - y[i])
    return out

# Calculates the error of the integration if given table
def TrapErrorTable(y,a,b,h):
    try:
        dy = DifferenceTable(y)
        dy2 = DifferenceTable(dy)
        avgdy2 = sum(dy2)/len(dy2)
        return (h**2 * (b-a) * avgdy2)/12
    except ZeroDivisionError:
        return 0

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
        self.y_values = []

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
            if not intervals or n <= 0 or n != int(intervals):
                raise ValueError
        except ValueError:
            show_alert("Please enter a valid whole positive number for intervals.")
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
        for i in range(1, self.table.columnCount()):
            item = self.table.item(1, i)
            if not item or not item.text().strip():
                show_alert("Please enter valid numbers for all y values.")
                return

            try:
                float_value = float(item.text())
            except ValueError:
                show_alert("Please enter valid numbers for all y values.")
                return

            # Append valid y value to y_values array
            self.y_values.append(float_value)

        # Check if all y values are valid
        if len(self.y_values) == self.table.columnCount() - 1:
            try:
                a = float(self.lower_bound_input.text())
                b = float(self.upper_bound_input.text())
                n = int(self.intervals_input.text())
                h = (b - a) / n

                # Use the TrapezoidalTable function with valid inputs
                result = TrapezoidalTable(h, self.y_values)

                # Placeholder for your error calculation
                error = TrapErrorTable(self.y_values,a,b,h)

                # Display the result and error
                self.result_label.setText(f"Result: {result}")
                self.error_label.setText(f"Error: {error}")
            except Exception as e:
                show_alert("Error during calculations.")
                return
        else:
            # Clear y_values array if not all y values are valid
            self.y_values = []
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

        description = (
            "Trapezoidal Integration is a technique for numerical integration which works by taking intervals and "
            "approximating them into trapezoids then calculating its area.\n"
            "It's not as accurate as the rest of the numerical integration methods as its order of error is O(h^2). "
            "You can increase the accuracy of the calculations by increasing the number of intervals."
        )

        formula = (
            "Integration from a to b f(x) = h/2 * (F(a) + 2 * summation from i = 1 to n-1 F(xi) + F(b))"
        )

        # Create widgets
        self.about_textbox = QTextEdit(self)
        self.about_textbox.setPlainText(f"{description}\n\n{formula}")
        self.about_textbox.setReadOnly(True)

        # Set up layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.about_textbox)
        
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
                result = TrapezoidalFunction(func, a, b, n)
                if result == float('inf') or result == float('-inf'):
                    show_alert("Numerical integration failed, because the integral is divergent.")
                else:
                    error = TrapErrorFunction(func,a,b,(b-a)/n)
                    # Display the result
                    self.result_label.setText(f"Result: {result}")
                    self.error_label.setText(f"Error: {error}") 
            except Exception:
                show_alert("Incorrect function, you either entered an undefined function or used multiple variables.")

class TrapezoidalForm(QMainWindow):
    def __init__(self):
        super(TrapezoidalForm, self).__init__()

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
    main_app = TrapezoidalForm()
    main_app.show()
    sys.exit(app.exec_())