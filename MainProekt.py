# -*- coding: utf-8 -*-
import sys
import math
import datetime
from PyQt5 import uic
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication, QLabel, QPushButton, QWidget,QLCDNumber, QLineEdit)
from pickle import loads, dumps
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QIcon
from Ejiiiidnevnik import Ui_MainWindow
pos = ''
writ = {}
fl = False
openz=''

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.initUI()       
    def initUI(self):
        uic.loadUi('проект_ГО.ui', self)
        self.make_2.clicked.connect(self.run)

        self.pushButton.clicked.connect(self.m)
        self.delete_z.clicked.connect(self.dele)
        self.label.setText('Нет заметок')
        self.listWidget.itemClicked.connect(self.list)
        
        openC = QAction(QIcon('calc.png'), 'Calculator', self)
        openC.setShortcut('Ctrl+O')
        openC.setStatusTip('Open Calculator')
        openC.triggered.connect(self.openc)
        openCalendar = QAction(QIcon('Calendar.png'), 'Calendar', self)
        openCalendar.setShortcut('Ctrl+P')
        openCalendar.setStatusTip('Open Calendar')
        openCalendar.triggered.connect(self.opencalendar)        
        menubar = self.menuBar
        fileMenu = menubar.addMenu('&Tools')
        fileMenu.addAction(openC)
        fileMenu.addAction(openCalendar)

        self.show()
        
    def openc(self):
        self.c = Calculator()
        self.c.show()
    
    def opencalendar(self):
        self.ca = Calendar()
        self.ca.show()        
        
    def dele(self):
        global writ
        self.listWidget.clear()
        a=self.lineEdit.text()
        if a in writ:
            del writ[a]
            self.listWidget.addItems(list(writ.keys()))
            if len(writ) != 0:
                self.label.clear()
                self.label.setText('Заметок:  ' + str(len(writ)))
            else:
                self.label.setText('Нет заметок')
        else:
            self.lineEdit.clear()
            self.lineEdit.setText('Нет заметки')
    
    def run(self):

        self.c = Example()

        self.c.show()  

    def m(self):
        global writ
        global fl
        global pos
        if len(writ) != 0:
            self.label.setText('Заметок:  ' + str(len(writ)))
        else:
            self.label.setText('Нет заметок')
        if fl:
            fl = False
            self.listWidget.addItems([pos])
        else:
            self.label.setText('Нужно создать заметку')

    def list(self, button):
        global openz
        global writ
        openz=button.text()
        self.c = Zam_text()

        self.c.show()
        

class Calendar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calendar.ui',self)
        
        
class Calculator(QMainWindow, QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        uic.loadUi('калькуляторр.ui', self)
        self.b_eq.clicked.connect(self.run)
        self.b_1.clicked.connect(self.run_1)
        self.b_2.clicked.connect(self.run_2)
        self.b_3.clicked.connect(self.run_3)
        self.b_4.clicked.connect(self.run_4)
        self.b_5.clicked.connect(self.run_5)
        self.b_6.clicked.connect(self.run_6)
        self.b_7.clicked.connect(self.run_7)
        self.b_8.clicked.connect(self.run_8)
        self.b_9.clicked.connect(self.run_9)
        self.b_0.clicked.connect(self.run_0)
        self.b_left.clicked.connect(self.run_left)
        self.b_right.clicked.connect(self.run_right)
        self.b_p.clicked.connect(self.run_p)
        self.b_back.clicked.connect(self.run_back)
        self.b_c.clicked.connect(self.run_c)
        self.b_pi.clicked.connect(self.run_pi)
        self.b_e.clicked.connect(self.run_e)
        self.b_fact.clicked.connect(self.run_fact)
        self.b_sin.clicked.connect(self.run_sin)
        self.b_root.clicked.connect(self.run_root)
        self.b_root3.clicked.connect(self.run_root3)

    def run(self):
        a = self.label.text()
        c = 0
        fact = None
        root = None
        st = None
        root3 = None
        for i in a:
            if i == '!':
                fact = c
            elif i == '√':
                root = i
            elif i == '^':
                st = i
            elif i == '∛':
                root3 = c
            c += 1

        print(eval(a))

    def run_1(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '1')

    def run_2(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '2')

    def run_3(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '3')

    def run_4(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '4')

    def run_5(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '5')

    def run_6(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '6')

    def run_7(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '7')

    def run_8(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '8')

    def run_9(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '9')

    def run_0(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '0')

    def run_left(self):
        if self.str_count.text() == '' or self.str_count.text()[-1] in ['+', '^', '-', '/', '√',
                                                                        '∛']:
            self.str_count.setText(self.str_count.text() + '(')

    def run_right(self):
        a = self.str_count.text()
        c = 0
        for i in a:
            if i == '(':
                c += 1
            elif i == ')':
                c -= 1
        if c >= 1:
            self.str_count.setText(self.str_count.text() + ')')
        else:
            self.str_count.setText(self.str_count.text() + '')

    def run_p(self):
        self.str_count.setText(self.str_count.text() + '.')

    def run_back(self):
        a = self.str_count.text()
        self.str_count.setText(a[:len(a) - 1])

    def run_c(self):
        self.str_count.clear()

    def run_pi(self):
        a = self.str_count.text()
        if a == '' or a[-1] in ['+', '^', '-', '/', '√', '∛']:
            self.str_count.setText(a + 'п')

    def run_e(self):
        a = self.str_count.text()
        if a == '' or a[-1] in ['+', '^', '-', '/', '√', '∛']:
            self.str_count.setText(a + 'e')

    def run_plus(self):
        self.str_count.setText(self.str_count.text() + '+')

    def run_minus(self):
        self.str_count.setText(self.str_count.text() + '-')

    def run_mult(self):
        self.str_count.setText(self.str_count.text() + '*')

    def run_st(self):
        self.str_count.setText(self.str_count.text() + '^')

    def run_split(self):
        self.str_count.setText(self.str_count.text() + '/')

    def run_fact(self):
        self.str_count.setText(self.str_count.text() + '!')

    def run_sin(self):
        a = self.str_count.text()
        if a == '' or a[-1] in ['+', '^', '-', '/', '√', '∛']:
            self.str_count.setText(self.str_count.text() + 'sin(')
    def run_root(self):
        a = self.str_count.text()
        self.str_count.setText(self.str_count.text() + '√')
    def run_root3(self):
        a = self.str_count.text()
        self.str_count.setText(self.str_count.text() + '∛')

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('создать заметку.ui', self)
        self.save_2.clicked.connect(self.save)
        self.show()
        
    def save(self):
        global writ
        global fl
        global pos
        fl = True
        writ[self.lineEdit.text()] = self.textEdit.toPlainText()
        pos = self.lineEdit.text()
        self.close()
        
class Zam_text(QMainWindow):
    def __init__(self):
        global writ
        global openz
        super().__init__()
        uic.loadUi('open_zamet.ui', self)
        self.textEdit.setPlainText(writ[openz])
        self.save_z.clicked.connect(self.red)
        self.show()

    def red(self):
        global writ
        writ[openz]=self.textEdit.toPlainText()
        self.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
