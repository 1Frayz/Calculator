from PyQt5 import QtCore, QtGui, QtWidgets
from functions import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.resize(400, 600)
        self.setMinimumSize(QtCore.QSize(400, 600))
        self.setMaximumSize(QtCore.QSize(400, 600))
        self.lineEdit = self.display(self, '', 20, 40, 0)
        self.lineEdit_2 = self.display(self, '0', 35, 60, 40)
        self.Button_1 = self.Button(self, 'ln', 4, 102).clicked.connect(lambda: function.log_e(self))
        self.Button_2 = self.Button(self, 'CE', 103, 102).clicked.connect(lambda: function.clear_all(self))
        self.Button_3 = self.Button(self, 'C', 202, 102).clicked.connect(lambda: function.clear(self))
        self.Button_4 = self.Button(self, '⌫', 301, 102).clicked.connect(lambda: function.delete(self))
        self.Button_5 = self.Button(self, '1/x', 4, 185).clicked.connect(lambda: function.fraction(self))
        self.Button_6 = self.Button(self, 'x²', 103, 185).clicked.connect(lambda: function.degree(self))
        self.Button_7 = self.Button(self, '²√x', 202, 185).clicked.connect(lambda: function.radical(self))
        self.Button_8 = self.Button(self, '/', 301, 185).clicked.connect(lambda: function.sign_click(self))
        self.Button_9 = self.Button(self, '7', 4, 268).clicked.connect(lambda: function.number_click(self))
        self.Button_10 = self.Button(self, '8', 103, 268).clicked.connect(lambda: function.number_click(self))
        self.Button_11 = self.Button(self, '9', 202, 268).clicked.connect(lambda: function.number_click(self))
        self.Button_12 = self.Button(self, '*', 301, 268).clicked.connect(lambda: function.sign_click(self))
        self.Button_13 = self.Button(self, '4', 4, 350).clicked.connect(lambda: function.number_click(self))
        self.Button_14 = self.Button(self, '5', 103, 350).clicked.connect(lambda: function.number_click(self))
        self.Button_15 = self.Button(self, '6', 202, 350).clicked.connect(lambda: function.number_click(self))
        self.Button_16 = self.Button(self, '-', 301, 350).clicked.connect(lambda: function.sign_click(self))
        self.Button_17 = self.Button(self, '1', 4, 433).clicked.connect(lambda: function.number_click(self))
        self.Button_18 = self.Button(self, '2', 103, 433).clicked.connect(lambda: function.number_click(self))
        self.Button_19 = self.Button(self, '3', 202, 433).clicked.connect(lambda: function.number_click(self))
        self.Button_20 = self.Button(self, '+', 301, 433).clicked.connect(lambda: function.sign_click(self))
        self.Button_21 = self.Button(self, '-/+', 4, 516).clicked.connect(lambda: function.switch(self))
        self.Button_22 = self.Button(self, '0', 103, 516).clicked.connect(lambda: function.number_click(self))
        self.Button_23 = self.Button(self, '.', 202, 516).clicked.connect(lambda: function.dot_click(self))
        self.Button_24 = self.Button(self, '=', 301, 516).clicked.connect(lambda: function.equals(self))
        self.show()

    @staticmethod
    def Button(link, text, x, y):
        button = QtWidgets.QPushButton(text, link)
        button.setGeometry(x, y, 95, 81)
        button.setMinimumSize(QtCore.QSize(95, 81))
        button.resize(95, 81)
        button.setMaximumSize(QtCore.QSize(95, 81))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        button.setFont(font)
        return button

    @staticmethod
    def display(link, text, size, y, y1):
        lineEdit = QtWidgets.QLineEdit(link)
        lineEdit.setGeometry(QtCore.QRect(4, y1, 392, y))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        font.setPointSize(size)
        font.setBold(False)
        font.setWeight(75)
        lineEdit.setFont(font)
        lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        lineEdit.setPlaceholderText(text)
        lineEdit.setReadOnly(True)
        return lineEdit


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec())
