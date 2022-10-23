import string
import math
from window import MainWindow
from PyQt5.QtWidgets import QApplication


def sqr(number):
    return pow(number, 2)


def sqrt(number):
    return pow(number, 0.5)


def ln(number):
    return math.log(number)


class function(MainWindow):
    def __init__(self):
        MainWindow.__init__(self)

    def number_click(self):
        if self.lineEdit.placeholderText() != '' and self.lineEdit.placeholderText()[-1] in '=)d':
            self.lineEdit_2.setPlaceholderText('0')
            self.lineEdit.setPlaceholderText('')
        if self.lineEdit_2.placeholderText() == '0':
            self.lineEdit_2.setPlaceholderText('')
        self.lineEdit_2.setPlaceholderText(self.lineEdit_2.placeholderText() + QApplication.instance().sender().text())

    def switch(self):
        self.lineEdit_2.setPlaceholderText(str(round(eval(f'-1 * {self.lineEdit_2.placeholderText()}'), 4)))

    def log_e(self):
        if self.lineEdit_2.placeholderText() == '0':
            return self.lineEdit.setPlaceholderText('Not determined')
        self.lineEdit.setPlaceholderText(f'ln({self.lineEdit_2.placeholderText()})')
        self.lineEdit_2.setPlaceholderText(str(round(eval(self.lineEdit.placeholderText()), 4)))

    def equals(self):
        if self.lineEdit_2.placeholderText() == '0' and self.lineEdit.placeholderText()[-1] == '/':
            return self.lineEdit.setPlaceholderText('Cant divide by 0')
        self.lineEdit.setPlaceholderText(self.lineEdit.placeholderText() + self.lineEdit_2.placeholderText())
        memory = str(round(eval(self.lineEdit.placeholderText()), 4))
        self.lineEdit.setPlaceholderText(self.lineEdit.placeholderText() + '=')
        self.lineEdit_2.setPlaceholderText(memory)

    def clear_all(self):
        self.lineEdit_2.setPlaceholderText('0')
        self.lineEdit.setPlaceholderText('')

    def clear(self):
        self.lineEdit_2.setPlaceholderText('0')

    def delete(self):
        if len(self.lineEdit_2.placeholderText()) == 1:
            self.lineEdit_2.setPlaceholderText('0')
        else:
            self.lineEdit_2.setPlaceholderText(self.lineEdit_2.placeholderText()[:-1])

    def fraction(self):
        if self.lineEdit_2.placeholderText() == '0':
            return self.lineEdit.setPlaceholderText('Cant divide by 0')
        self.lineEdit.setPlaceholderText(f'1/{self.lineEdit_2.placeholderText()}')
        self.lineEdit_2.setPlaceholderText(str(round(eval(self.lineEdit.placeholderText()), 4)))
        self.lineEdit.setPlaceholderText(self.lineEdit.placeholderText() + '=')

    def radical(self):
        if self.lineEdit_2.placeholderText()[0] == '-':
            return self.lineEdit.setPlaceholderText('The number is negative')
        self.lineEdit.setPlaceholderText(f'sqrt({self.lineEdit_2.placeholderText()})')
        self.lineEdit_2.setPlaceholderText(str(round(eval(self.lineEdit.placeholderText()), 4)))

    def degree(self):
        self.lineEdit.setPlaceholderText(f'sqr({self.lineEdit_2.placeholderText()})')
        self.lineEdit_2.setPlaceholderText(str(round(eval(self.lineEdit.placeholderText()), 4)))

    def dot_click(self):
        if '.' in self.lineEdit_2.placeholderText():
            return
        else:
            self.lineEdit_2.setPlaceholderText(self.lineEdit_2.placeholderText() + '.')

    def sign_click(self):
        if self.lineEdit.placeholderText() != '' and self.lineEdit.placeholderText()[-1] not in string.digits:
            self.lineEdit.setPlaceholderText(self.lineEdit.placeholderText()[:-1] + QApplication.instance().sender().text())
        else:
            self.lineEdit.setPlaceholderText(self.lineEdit_2.placeholderText() + QApplication.instance().sender().text())
        self.lineEdit_2.setPlaceholderText('0')

