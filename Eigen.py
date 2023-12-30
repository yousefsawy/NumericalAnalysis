import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit, QTextEdit, QTabWidget

from eigenvalue import Ui_MainWindow
from eigen_logic import maxeigen, mineigen, max_deflation_matrix, min_deflation_matrix, secondmax, secondmin

class AboutPage(QWidget):
    def __init__(self):
        super(AboutPage, self).__init__()
        
        # Create widgets
        self.about_textbox = QTextEdit(self)
        self.about_textbox.setPlainText("""In linear algebra, eigenvalues are a special set of numbers associated with a square matrix. They represent the scaling factor by which a vector is stretched or compressed when multiplied by that matrix. Eigenvalues are often used in various mathematical and scientific applications, such as solving systems of linear equations and analyzing the behavior of dynamical systems. 

            There is one common numerical method to solve for eigenvalues called the power iteration method. Here's a simplified explanation:

            1. Start with an initial guess for an eigenvector.
            2. Multiply the matrix by the eigenvector to get a new vector.
            3. Normalize the new vector.
            4. Repeat steps 2 and 3 several times until the vector converges to the dominant eigenvector.
            5. The corresponding eigenvalue is the ratio of the new vector to the previous vector.

This method can be iterated to find additional eigenvalues and eigenvectors. There are also other numerical methods available, depending on the specific problem and matrix properties.""")

        self.about_textbox.setReadOnly(True)

        # Set up layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.about_textbox)
        # Increase font size
        font = self.about_textbox.font()
        font.setPointSize(12)  # Adjust the size as needed
        self.about_textbox.setFont(font)

class Eigen(QMainWindow):

    def __init__(self):
        super().__init__()
        self.OpenEigen()
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_2.clicked.connect(self.initInput)
        self.ui.pushButton.clicked.connect(self.executeFunc)
                
    def OpenEigen(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def initInput(self):
        self.ValidateInputN()
        self.initInputMatrix()
        self.initInputVector()

    def ValidateInputN(self):
        try:
            self.N = int(self.ui.lineEdit_2.text())
            if (self.N<1):
                raise Exception("N should be a positive integer")
        except:
            self.show_warning_messagebox('N should be an integer')
            return
        
    def initInputMatrix(self):
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.horizontalHeader().setVisible(False)  
        self.InitRowsAndColumns()

    def InitRowsAndColumns(self):
        self.ui.tableWidget.setColumnCount(self.N)
        self.ui.tableWidget.setRowCount(self.N)
        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                item = QTableWidgetItem('')
                self.ui.tableWidget.setItem(row, col, item)
            self.ui.tableWidget.setRowHeight(row,int(160/self.N))
        
        for col in range(self.ui.tableWidget.columnCount()):
            self.ui.tableWidget.setColumnWidth(col, int(320 / (self.N + 1)))
        
    def initInputVector(self):
        self.ui.tableWidget_2.setRowCount(self.N)
        self.ui.tableWidget_2.setColumnCount(1)
        self.ui.tableWidget_2.verticalHeader().setVisible(False)
        self.ui.tableWidget_2.horizontalHeader().setVisible(False) 
        for row in range(self.ui.tableWidget_2.rowCount()):
            item = QTableWidgetItem('')
            self.ui.tableWidget_2.setItem(row,0, item)
            self.ui.tableWidget_2.setColumnWidth(row, 40)
            self.ui.tableWidget_2.setRowHeight(row, int(160/self.N))
    
    def ValidateMatrixInputs(self):
        self.matrix = []
        try:
            for row in range(self.N):
                OneRow = []
                for col in range(self.N):
                    OneRow.append(float(self.ui.tableWidget.item(row, col).text()))
                self.matrix.append(OneRow)
        except:
            self.show_warning_messagebox('Invalid Matrix Input')
            return
        
    def ValidateVectorInputs(self):
        self.vector = []
        try:
            for row in range(self.N):
                self.vector.append(float(self.ui.tableWidget_2.item(row,0).text()))
            print("ana el vector", self.vector)
        except Exception as e:
            print(f'Exception: {e}')
            self.show_warning_messagebox('Invalid Vector Input')
            return

    
    def ValidateIterations(self):
        try:
            self.iterations = int(self.ui.lineEdit_3.text())
            if (self.iterations<1):
                raise Exception("Iterations No. should be a positive integer")
        except:
            self.show_warning_messagebox('iterations number should be an integer')
            return

    def ValidateInput(self):
        self.ValidateMatrixInputs()
        self.ValidateVectorInputs()
        self.ValidateIterations()


    def executeFunc(self):
        self.ValidateInput()
        self.defMatrix=[]
        try:
            self.ChooseFunc()
        except:
            self.show_warning_messagebox('Error During Calculation.')
                   
        if (self.defMatrix!=[]):
            self.ShowFinalMatrix()
        self.ShowLamda()
        self.ShowVector()

    def ChooseFunc(self):
        if (self.ui.radioButton_1.isChecked()==True):
            self.eigen= maxeigen(self.matrix, self.vector, self.iterations)
        if (self.ui.radioButton_2.isChecked()==True):
            self.eigen= mineigen(self.matrix, self.vector, self.iterations)
        if (self.ui.radioButton_3.isChecked()==True):
            self.eigen= maxeigen(self.matrix, self.vector, self.iterations)
            lamda_max, x = self.eigen
            self.defMatrix = max_deflation_matrix(self.matrix, self.vector, lamda_max)
        if (self.ui.radioButton_4.isChecked()==True):
            self.eigen= mineigen(self.matrix, self.vector, self.iterations)
            lamda_min, x = self.eigen
            self.defMatrix = min_deflation_matrix(self.matrix, self.vector, lamda_min)
        if (self.ui.radioButton_5.isChecked()==True):
            lamda_max, x= maxeigen(self.matrix, self.vector, self.iterations)
            self.defMatrix= max_deflation_matrix(self.matrix, self.vector, lamda_max)
            self.eigen = secondmax(self.defMatrix, self.vector, self.iterations)
        if (self.ui.radioButton_6.isChecked()==True):
            lamda_min, x= mineigen(self.matrix, self.vector, self.iterations)
            self.defMatrix= min_deflation_matrix(self.matrix, self.vector, lamda_min)
            self.eigen = secondmin(self.defMatrix, self.vector, self.iterations)

    def ShowFinalMatrix(self):
        self.ui.tableWidget_3.setColumnCount(self.N)
        self.ui.tableWidget_3.setRowCount(self.N)
        self.ui.tableWidget_3.verticalHeader().setVisible(False)
        self.ui.tableWidget_3.horizontalHeader().setVisible(False)
        for row in range(self.N):
            for col in range(self.N):
                item = QTableWidgetItem(str(self.defMatrix[row][col]))
                self.ui.tableWidget_3.setItem(row, col, item)
                self.ui.tableWidget_3.setColumnWidth(col, int(170/(self.N)))
            self.ui.tableWidget_3.setRowHeight(row, int(90/(self.N)))

    def ShowVector(self):
        self.ui.tableWidget_4.setColumnCount(1)
        self.ui.tableWidget_4.setRowCount(self.N)
        self.ui.tableWidget_4.verticalHeader().setVisible(False)
        self.ui.tableWidget_4.horizontalHeader().setVisible(False) 
        for row in range(self.N):
            item = QTableWidgetItem(str(self.eigen[1][row]))
            self.ui.tableWidget_4.setItem(row, 0, item)
            self.ui.tableWidget_4.setColumnWidth(0, 51)
        self.ui.tableWidget_3.setRowHeight(row, int(120/(self.N)))

    def ShowLamda(self):
        self.ui.textBrowser.setText(str(self.eigen[0]))

    def show_warning_messagebox(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Wrong Input")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = msg.exec_()

class EigenForm(QMainWindow):
    def __init__(self):
        super(EigenForm, self).__init__()

        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # Create and add the pages to the tab widget
        self.function_page = Eigen()
        self.about_page = AboutPage()

        self.tab_widget.addTab(self.function_page, "Calculation")
        self.tab_widget.addTab(self.about_page, "About")

        # Show the default tab
        self.tab_widget.setCurrentIndex(0)
        self.setStyleSheet("""
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
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = EigenForm()
    main_app.show()
    sys.exit(app.exec_())