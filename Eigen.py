
class eigen()


def initInputMatrix(self):
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.horizontalHeader().setVisible(False)  
        self.InitRowsAndColumns()

    def InitRowsAndColumns(self):
        self.ui.tableWidget.setColumnCount(self.N+1)
        self.ui.tableWidget.setRowCount(self.N)
        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                item = QTableWidgetItem('')
                self.ui.tableWidget.setItem(row, col, item)
            self.ui.tableWidget.setRowHeight(row,int(190/self.N))
        
        for col in range(self.ui.tableWidget.columnCount()):
            self.ui.tableWidget.setColumnWidth(col, int(250 / (self.N + 1)))
        
    def initInputVector(self):
        self.ui.tableWidget_2.setColumnCount(self.N)
        self.ui.tableWidget_2.setRowCount(1)
        self.ui.tableWidget_2.verticalHeader().setVisible(False)
        self.ui.tableWidget_2.horizontalHeader().setVisible(False) 
        for col in range(self.ui.tableWidget_2.columnCount()):
            item = QTableWidgetItem('')
            self.ui.tableWidget_2.setItem(0, col, item)
            self.ui.tableWidget_2.setColumnWidth(col, int(250/(self.N)))
    
    def ValidateMatrixInputs(self):
        self.matrix = []
        try:
            for row in range(self.N):
                OneRow = []
                for col in range(self.N + 1):
                    OneRow.append(float(self.ui.tableWidget.item(row, col).text()))
                self.matrix.append(OneRow)
        except:
            self.show_warning_messagebox('Invalid Matrix Input')
            return
        
    def ValidateVectorInputs(self):
        self.vector = [0]*self.N
        try:
            for col in range(self.N):
                self.vector[col]=(float(self.ui.tableWidget.item(0, col).text()))
        except:
            self.show_warning_messagebox('Invalid Vector Input')
            return

    def ValidateIterations(self):
            try:
                self.iterations = int(self.ui.lineEdit_2.text())
                if (self.iterations<1):
                    raise Exception("Iterations No. should be a positive integer")
            except:
                self.show_warning_messagebox('iterations number should be an integer')
                return

    def ValidateInput(self):
        self.ValidateMatrixInputs()
        self.ValidateVectorInputs()
        self.ValidateW()
        self.ValidateIterations()

    def initInput(self):
            self.ValidateInputN()
            self.initInputMatrix()
            self.initInputVector()

    def ValidateInputN(self):
        try:
            self.N = int(self.ui.lineEdit.text())
            if (self.N<1):
                raise Exception("N should be a positive integer")
        except:
            self.show_warning_messagebox('N should be an integer')
            return