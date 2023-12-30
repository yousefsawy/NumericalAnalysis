# Import necessary PyQt5 modules and libraries for plotting
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QRadioButton, QPushButton, \
    QHBoxLayout, QSizePolicy, QTextEdit, QMainWindow
from PyQt5.QtGui import QTextDocument, QFont, QTextOption
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, prod

# Define the main class for the Lagrange Interpolation Calculator
class LagrangeInterpolationCalculator(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the graph canvas variable
        self.graph_canvas = None  # Store the FigureCanvas instance

        # Set up the user interface
        self.init_ui()

    def init_ui(self):
        # Create widgets
        # Label for providing instructions
        self.instructions_label = QLabel()
        self.instructions_label.setTextFormat(Qt.RichText)
        self.instructions_label.setText(self.generate_instructions_html())

        # Labels and input fields for X and Y values
        self.label_X = QLabel("Enter array of X (space-separated):")
        self.label_X.setFont(QFont('Arial', 14))
        self.entry_X = QLineEdit()
        self.entry_X.setFont(QFont('Arial', 14))

        self.label_Y = QLabel("Enter array of Y (space-separated):")
        self.label_Y.setFont(QFont('Arial', 14))
        self.entry_Y = QLineEdit()
        self.entry_Y.setFont(QFont('Arial', 14))

        # Radio buttons for selecting the type of calculation
        self.radio_Y_to_X = QRadioButton("Calculate Y based on X")
        self.radio_Y_to_X.setFont(QFont('Arial', 14))
        self.radio_X_to_Y = QRadioButton("Calculate X based on Y")
        self.radio_X_to_Y.setFont(QFont('Arial', 14))

        # Label and input field for interpolation value
        self.label_interpolation = QLabel("Enter interpolation value:")
        self.label_interpolation.setFont(QFont('Arial', 14))
        self.entry_interpolation = QLineEdit()
        self.entry_interpolation.setFont(QFont('Arial', 14))

        # Button to trigger the calculation
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.setFont(QFont('Arial', 16, QFont.Bold))

        # Label to display calculation results
        self.result_label = QLabel("Result:")
        self.result_label.setFont(QFont('Arial', 16, QFont.Bold))

        # Label for the graph
        self.label_graph = QLabel("Graph:")
        self.label_graph.setFont(QFont('Arial', 16, QFont.Bold))

        # Placeholder for the graph
        self.graph_placeholder = QWidget()
        self.graph_placeholder.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # TextEdit widget for providing instructions (HTML formatted)
        self.instructions_label = QTextEdit()
        self.instructions_label.setText(self.generate_instructions_html())
        self.instructions_label.setReadOnly(True)
        self.instructions_label.setWordWrapMode(QTextOption.WordWrap)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.instructions_label)  # Add the instructions label
        layout.addWidget(self.label_X)
        layout.addWidget(self.entry_X, 0, Qt.AlignLeft)  # Align to the left
        layout.addWidget(self.label_Y)
        layout.addWidget(self.entry_Y, 0, Qt.AlignLeft)  # Align to the left
        layout.addWidget(self.radio_Y_to_X)
        layout.addWidget(self.radio_X_to_Y)
        layout.addWidget(self.label_interpolation)
        layout.addWidget(self.entry_interpolation)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.label_graph, 0, Qt.AlignLeft)  # Align to the left
        layout.addWidget(self.graph_placeholder)  # Add the placeholder for the graph

        # Set the vertical spacing (padding) between widgets
        layout.setSpacing(10)

        self.setLayout(layout)
        # self.setFixedSize(1000, 1000)  # Set fixed width and height

        # Connect the button click to the calculate function
        self.calculate_button.clicked.connect(self.calculate)

        # Adjust the size policy and width constraints for certain widgets
        self.adjust_field_sizes()

    def adjust_field_sizes(self):
        # Adjust the size policy and width constraints for certain widgets
        for widget in [self.label_X, self.entry_X, self.label_Y, self.entry_Y, self.radio_Y_to_X,
                       self.radio_X_to_Y, self.label_interpolation, self.entry_interpolation, self.result_label]:
            widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            widget.setMaximumWidth(600)
            widget.setMinimumWidth(widget.sizeHint().width())

    def generate_instructions_html(self):
        # Generate HTML-formatted instructions for the user
        return """
        <p style="font-size:14pt; word-wrap: break-word;">Lagrange interpolation is a mathematical technique used to construct a polynomial that passes through a given set of data points</p>
        <p style="font-size:16pt; font-weight:bold; margin-bottom:0;">How it works:</p>
        <p style="font-size:14pt; word-wrap: break-word;">The Lagrange interpolating polynomial is constructed by summing up terms, each associated with a data point. Each term is a product of the corresponding y-coordinate and a set of fractional terms, where each fractional term involves the difference of 
x and the x-coordinate of a data point divided by the difference of x-coordinates for the current and all other data points and vice versa if the real root is required.</p>
        <p style="font-size:16pt; word-wrap: break-word; font-weight:bold; color:red; margin-top:10px; margin-bottom:0;">What to avoid:</p>
        <p style="color:red; font-size:11pt;">Caution against high-degree Lagrange interpolations to prevent oscillations and instability. Opt for non-equidistant data and address outliers cautiously. Mitigate precision issues and overfitting by selecting a suitable polynomial degree. Explore alternative interpolation methods for specific scenarios to enhance performance.</p>
        """

    def lagrange_interpolation(self, x, X, Y, switch):
        # Perform Lagrange interpolation for a given x and data points X, Y
        if switch:
            X, Y = Y, X
        n = len(X)
        result = 0
        for i in range(n):
            term = Y[i]
            for j in range(n):
                if i != j:
                    term *= (x - X[j]) / (X[i] - X[j])
            result += term
        return result

    def lagrange_derivative_interpolation(self, input_x, X, Y, switch):
        if switch:
            X, Y = Y, X
        n = len(X)  # get the length of the points to table to set the iteration
        result = 0.0
        x = symbols('x')  # corrected the variable name
        # Nested Loop
        for i in range(n):
            term = Y[i]  # catch the y value
            for j in range(n):
                if i != j:
                    term *= (x - X[j]) / (X[i] - X[j])
            term_diff = diff(term, x)  # corrected the method name
            result += term_diff.evalf(subs={x: input_x})

        return result

    def calculate(self):
        # Handle button click to perform calculations
        x_values = list(map(float, self.entry_X.text().split()))
        y_values = list(map(float, self.entry_Y.text().split()))
        x_to_interpolate = float(self.entry_interpolation.text())
        switch = self.radio_X_to_Y.isChecked()

        if switch:
            result_interp = self.lagrange_interpolation(x_to_interpolate, y_values, x_values, switch)
            result_derivative = self.lagrange_derivative_interpolation(x_to_interpolate, y_values, x_values, switch)
        else:
            result_interp = self.lagrange_interpolation(x_to_interpolate, x_values, y_values, switch)
            result_derivative = self.lagrange_derivative_interpolation(x_to_interpolate, x_values, y_values, switch)

        self.result_label.setText(f"Lagrange Interpolation: {result_interp:.8f}\nDerivative: {result_derivative:.8f}")

        # Update the graph
        self.update_graph(x_values, y_values, x_to_interpolate, switch)

    def update_graph(self, X, Y, x_to_interpolate, switch):
        # If the canvas is not created, create it
        if self.graph_canvas is None:
            self.graph_canvas = self.get_graph_canvas(X, Y, x_to_interpolate, switch)
            upper_text_space = QWidget()
            upper_text_space.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

            new_layout = QVBoxLayout(self.graph_placeholder)
            new_layout.addWidget(upper_text_space)
            new_layout.addWidget(self.graph_canvas)

        # If the canvas is already created, update its content
        else:
            self.graph_canvas.figure.clear()
            ax = self.graph_canvas.figure.add_subplot(111)
            x = np.linspace(min(X), max(X), 1000)
            y = [self.lagrange_interpolation(val, X, Y, switch) for val in x]

            ax.plot(X, Y, 'ro', label='Data Points')
            ax.plot(x, y, label='Interpolated Polynomial')
            ax.axvline(x=x_to_interpolate, color='g', linestyle='--', label=f'Interpolation Point ({x_to_interpolate:.2f})')
            ax.legend()
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_title('Lagrange Interpolation')

            self.graph_canvas.draw()

        self.instructions_label.setMinimumHeight(self.instructions_label.sizeHint().height())

    def get_graph_canvas(self, X, Y, x_to_interpolate, switch):
        # Create a graph canvas with the interpolated polynomial and data points
        x = np.linspace(min(X), max(X), 1000)
        y = [self.lagrange_interpolation(val, X, Y, switch) for val in x]

        fig, ax = plt.subplots()
        ax.plot(X, Y, 'ro', label='Data Points')
        ax.plot(x, y, label='Interpolated Polynomial')
        ax.axvline(x=x_to_interpolate, color='g', linestyle='--', label=f'Interpolation Point ({x_to_interpolate:.2f})')
        ax.legend()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Lagrange Interpolation')

        canvas = FigureCanvas(fig)
        return canvas


# Entry point of the program
if __name__ == '__main__':
    # Create the application instance
    app = QApplication([])

    # Create and show the Lagrange Interpolation Calculator window
    window = LagrangeInterpolationCalculator()
    window.setWindowTitle("Lagrange Interpolation Calculator")
    window.show()

    # Start the application event loop
    app.exec_()
