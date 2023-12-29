# Assuming you have a QMainWindow subclass
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QAction, QWidget, QVBoxLayout, QLabel, QTextEdit
from PyQt5.QtWidgets import  QHBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton

class PointsPage(QWidget):
    def __init__(self):
        super(PointsPage, self).__init__()

        # Create widgets
        self.upper_bound_label = QLabel("Upper Bound:")
        self.upper_bound_input = QLineEdit(self)

        self.lower_bound_label = QLabel("Lower Bound:")
        self.lower_bound_input = QLineEdit(self)

        self.intervals_label = QLabel("Intervals:")
        self.intervals_input = QLineEdit(self)

        self.show_table_button = QPushButton("Show Table", self)
        self.table = QTableWidget(self)

        self.show_result_button = QPushButton("Show Result", self)
        self.result_label = QLabel("Result:")
        self.error_label = QLabel("Error:")

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
        lower_bound = float(self.lower_bound_input.text())
        upper_bound = float(self.upper_bound_input.text())
        intervals = int(self.intervals_input.text())

        # Calculate x values based on the given bounds and intervals
        x_values = [round(lower_bound + i * ((upper_bound - lower_bound) / intervals), 2) for i in range(intervals + 1)]

        # Set up the table
        self.table.setRowCount(2)
        self.table.setColumnCount(intervals + 1)
        self.table.setHorizontalHeaderLabels(map(str, x_values))

        # Fill the x row
        for i in range(intervals + 1):
            item = QTableWidgetItem(str(x_values[i]))
            self.table.setItem(0, i, item)

    def show_result(self):
        # Placeholder for your result calculation
        result = "Result: N/A"
        error = "Error: N/A"

        # Display the result and error
        self.result_label.setText(result)
        self.error_label.setText(error)


class AboutPage(QWidget):
    def __init__(self):
        super(AboutPage, self).__init__()

        # Create widgets
        self.about_textbox = QTextEdit(self)
        self.about_textbox.setPlainText("About section here")
        self.about_textbox.setReadOnly(True)

        # Set up layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.about_textbox)


class FunctionPage(QWidget):
    def __init__(self):
        super(FunctionPage, self).__init__()

        # Create widgets
        self.function_label = QLabel("Function:")
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
        lower_bound = float(self.lower_bound_input.text())
        upper_bound = float(self.upper_bound_input.text())
        intervals = int(self.intervals_input.text())

        # Perform calculation (replace this with your actual function calculation)
        result = self.calculate_function_result(function_str, lower_bound, upper_bound, intervals)

        # Display the result
        self.result_label.setText(f"Result: {result}")
        self.error_label.setText("Error: N/A")  # You can calculate and display an error if needed

    def calculate_function_result(self, function_str, lower_bound, upper_bound, intervals):
        # Placeholder function, replace this with your actual function calculation
        # For simplicity, let's just calculate the sum of values within the given bounds
        step_size = (upper_bound - lower_bound) / intervals
        result = sum(eval(function_str.replace('x', str(lower_bound + i * step_size))) for i in range(intervals))
        return result


class TrapezoidalForm(QMainWindow):
    def __init__(self):
        super(TrapezoidalForm, self).__init__()

        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Create actions
        self.function_action = QAction('Function', self)
        self.points_action = QAction('Points', self)
        self.about_action = QAction('About', self)

        # Connect actions to slots
        self.function_action.triggered.connect(self.show_function_page)
        self.points_action.triggered.connect(self.show_points_page)
        self.about_action.triggered.connect(self.show_about_page)

        # Add actions to menu bar
        menu_bar = self.menuBar()
        function_menu = menu_bar.addMenu('Function')
        function_menu.addAction(self.function_action)

        points_menu = menu_bar.addMenu('Points')
        points_menu.addAction(self.points_action)

        about_menu = menu_bar.addMenu('About')
        about_menu.addAction(self.about_action)

        # Create and add the pages to the stacked widget
        self.function_page = FunctionPage()
        self.points_page = PointsPage()
        self.about_page = AboutPage()

        self.stacked_widget.addWidget(self.function_page)
        self.stacked_widget.addWidget(self.points_page)
        self.stacked_widget.addWidget(self.about_page)

        # Show the default page
        self.show_function_page()

    def show_function_page(self):
        self.stacked_widget.setCurrentWidget(self.function_page)

    def show_points_page(self):
        self.stacked_widget.setCurrentWidget(self.points_page)

    def show_about_page(self):
        self.stacked_widget.setCurrentWidget(self.about_page)
