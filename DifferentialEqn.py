import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QSizePolicy, QComboBox, QSpinBox, QPushButton
from PyQt5.QtGui import QFont


class DifferentialEquationSolver(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(5)  # Adjust vertical spacing

        # Instructions area
        instructions_text = """
<h2 style="font-weight: bold; font-size: 16px;">Euler's Method:</h2>
<p style="font-size: 14px;">Euler's method is a simple and straightforward numerical technique for solving first-order ODEs.
It is based on the idea of approximating the solution curve by moving along the tangent line at each point.</p>

<h2 style="font-weight: bold; font-size: 16px;">Heun's Method (Improved Euler Method):</h2>
<p style="font-size: 14px;">Heun's method is an improvement over Euler's method, providing more accuracy by considering the average of two estimates of the slope.

In both methods, the solution is iteratively approximated by stepping through the independent variable (x) in small increments.
The choice of step size (h) is calculated by X_target-Xi

These methods are particularly useful for solving initial value problems where the value of the function and its derivative are known at a specific initial point,
and the goal is to approximate the function at other points.</p>
"""

        instructions_area = QTextEdit(self)
        instructions_area.setHtml(instructions_text)
        instructions_area.setReadOnly(True)
        instructions_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # Set size policy to Expanding vertically
        self.layout.addWidget(instructions_area)

        # Labels and Combobox
        self.order_label = QLabel('Choose Order:', self)
        self.layout.addWidget(self.order_label)
        self.order_combo = QComboBox(self)
        self.order_combo.addItems(['First Order', 'Second Order'])
        self.layout.addWidget(self.order_combo)

        self.method_label = QLabel('Choose Method:', self)
        self.layout.addWidget(self.method_label)
        self.method_combo = QComboBox(self)
        self.method_combo.addItems(['Euler', 'Heun'])
        self.layout.addWidget(self.method_combo)

        self.equation_label = QLabel('Differential Equation: (example: write y\' = xy + x^2  as x*y + x**2)', self)
        self.layout.addWidget(self.equation_label)
        self.equation_input = QLineEdit(self)
        self.layout.addWidget(self.equation_input)

        self.initial_value_x0_label = QLabel('Initial Value of x (x0):', self)
        self.layout.addWidget(self.initial_value_x0_label)
        self.initial_value_x0_input = QLineEdit(self)
        self.layout.addWidget(self.initial_value_x0_input)

        self.initial_value_y0_label = QLabel('Initial Value of y (y0):', self)
        self.layout.addWidget(self.initial_value_y0_label)
        self.initial_value_y0_input = QLineEdit(self)
        self.layout.addWidget(self.initial_value_y0_input)

        # Add labels and input fields for z
        self.initial_value_z0_label = QLabel('Initial Value of z (z0):', self)
        self.layout.addWidget(self.initial_value_z0_label)
        self.initial_value_z0_input = QLineEdit(self)
        self.layout.addWidget(self.initial_value_z0_input)

        self.target_x_label = QLabel('Target x-value:', self)
        self.layout.addWidget(self.target_x_label)
        self.target_x_input = QLineEdit(self)
        self.layout.addWidget(self.target_x_input)

        self.iterations_label = QLabel('Number of Iterations (Heun only):', self)
        self.layout.addWidget(self.iterations_label)
        self.iterations_input = QSpinBox(self)
        self.layout.addWidget(self.iterations_input)

        self.result_label = QLabel(self)
        self.layout.addWidget(self.result_label)

        # Solve Button
        self.solve_button = QPushButton('Solve', self)
        self.solve_button.clicked.connect(self.solve)
        self.layout.addWidget(self.solve_button)

        # Set the layout
        self.setLayout(self.layout)

        # Set the window properties
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Differential Equation Solver')

    def solve(self):
        try:
            selected_order = self.order_combo.currentText()
            selected_method = self.method_combo.currentText()
            equation = self.equation_input.text()
            initial_value_x0 = float(self.initial_value_x0_input.text())
            initial_value_y0 = float(self.initial_value_y0_input.text())

            # Check if z input is empty
            z_input_text = self.initial_value_z0_input.text().strip()

            try:
                initial_value_z0 = float(z_input_text)
            except ValueError:
                # Set default value for z if the input is empty or not a valid float
                initial_value_z0 = 0.0

            target_x = float(self.target_x_input.text())

            result_y = None

            if selected_order == 'First Order':
                if selected_method == 'Euler':
                    result_y = Euler(differential_equation, initial_value_x0, initial_value_y0, target_x, equation)
                elif selected_method == 'Heun':
                    # Pass 'equation' parameter to heun_method
                    iterations = self.iterations_input.value()
                    result_y = heun_method(differential_equation, equation, initial_value_x0, initial_value_y0, initial_value_z0, target_x, iterations)
                else:
                    raise ValueError('Invalid method selected.')

                self.result_label.setText(f"The estimated value of y at x = {target_x} is: {result_y}")
            elif selected_order == 'Second Order':
                # Add logic for second order differential equation
                pass
            else:
                raise ValueError('Invalid order selected.')

        except Exception as e:
            self.result_label.setText(f"Error: {str(e)}")


def Euler(func, x0, y0, x_target, equation):
    h = x_target - x0
    h = round(h, 6)
    x = x0
    y = y0
    y = y + h * func(x, y, 0, equation)  # Set z to 0 for first order
    return y
    

def heun_method(func, equation, x0, y0, z0, x_target, num_iterations):
    h = x_target - x0
    h = round(h, 6)
    x = x0
    y = y0
    z = z0

    for _ in range(num_iterations):
        k1 = h * func(x, y, z, equation)
        k2 = h * func(x + h, y + k1, z, equation)
        y = y + 0.5 * (k1 + k2)
        x += h

    return y


def differential_equation(x, y, z, equation):
    # Modify this function based on your differential equation
    return eval(equation.replace('^', '**').replace('x', str(x)).replace('y', str(y)).replace('z', str(z)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DifferentialEquationSolver()
    window.show()
    sys.exit(app.exec_())
