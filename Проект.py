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

#переменная отвечающая за добавление заметки в listWidget
pos = ''
#Словарь содержащие ключи-название заметки и значение ключа-содержимое заметки
writ = {}
#переменная отвечающая за запоминание открывающейся заметки на изменение
open_z=''
#последняя созданная заметка
last_z=[]

#Открытие уже существующих заметок(с помощью файла)
try:
    with open('list_z.txt', mode='rt') as f:
        f=f.read()
        f=f.split('\n')
        f=f[:len(f)-1]
        for i in f:
            i=i.split(';;;;;;#')
            writ[i[0]]=i[1]
except FileNotFoundError:
    writ={}
#гланый класс отвечающий за показ,удаление, создание,добавление и изменение заметки

class MyWidget(QMainWindow):
    #конструктор класса основа дизайна окна
    def __init__(self):
        super().__init__()
        uic.loadUi('проект_ГО.ui', self)
        self.make_2.clicked.connect(self.run)
        self.pushButton.clicked.connect(self.m)
        self.delete_z.clicked.connect(self.dele)
        self.label.setText('Нет заметок')
        self.listWidget.itemClicked.connect(self.list)
        if len(writ)!=0:
            self.listWidget.addItems(list(writ.keys()))        
        self.show()
    #Меню
        openC = QAction(QIcon('calc.png'), 'Calculator', self)
        openC.setShortcut('Ctrl+O')
        openC.setStatusTip('Open Calculator')
        openC.triggered.connect(self.openc)
        
        openCalendar = QAction(QIcon('Calendar.png'), 'Calendar', self)
        openCalendar.setShortcut('Ctrl+P')
        openCalendar.setStatusTip('Open Calendar')
        openCalendar.triggered.connect(self.opencalendar)       
        
        Del = QAction(QIcon('Delete all.png'), 'Delete all', self)
        Del.setShortcut('Ctrl+D')
        Del.setStatusTip('Delete all')
        Del.triggered.connect(self.delall)  
        
        menubar = self.menuBar
        fileMenu = menubar.addMenu('&Tools')
        fileMenu.addAction(openC)
        fileMenu.addAction(openCalendar)       
        fileMenu.addAction(Del) 
       
    #Открытие калькулятора   
    def openc(self):
        self.c = Calculator()
        self.c.show()
    #Открытие календаря
    def opencalendar(self):
        self.ca = Calendar()
        self.ca.show()
    #Удаление всех заметок
    def delall(self):
        self.listWidget.clear()    
    
    #закрытие приложения,сохранение данных
    def closeEvent(self,event):
        global writ
        with open('list_z.txt',mode='wt') as a:
            for i in writ.keys():
                a.write(i+';;;;;;#'+writ[i]+'\n')  
        self.close()
        
    #функция для удаления заметки
    def dele(self):
        global writ
        a=self.lineEdit.text()
        if a in writ:
            del writ[a]
            self.listWidget.clear()
            self.listWidget.addItems(list(writ.keys()))
            if len(writ) != 0:
                self.label.clear()
                self.label.setText('Заметок:  ' + str(len(writ)))
            else:
                self.label.setText('Нет заметок')
        else:
            self.lineEdit.clear()
            self.lineEdit.setText('Нет заметки')
    #функция открытия окна отвечающего за создания заметки
    def run(self):
        self.c = Example()
        self.c.show()
    #функция добавления заметки
    def m(self):
        global writ
        global pos
        global last_z
        
        if len(writ) == 0:
      
            self.label.setText('Нет заметок')
        if pos!='':
            writ[last_z[0]]=last_z[1]
            self.label.setText('Заметок:  ' + str(len(writ)))
            last_z=[]            
            self.listWidget.addItems([pos])
            pos=''
        else:
            self.label.setText('Нужно создать заметку')
    #функция открытия содержания заметки
    def list(self, button):
        global open_z
        global writ
        open_z=button.text()
        self.c = Zam_text()
        self.c.show()       
#Календарь
class Calendar(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calendar.ui',self)        
        
#класс отвечающий за создание названия и содержания заметки
class Example(QMainWindow):
    #конструктор класса основа дизайна окна
    def __init__(self):
        super().__init__()
        uic.loadUi('создать заметку.ui', self)
        self.save_2.clicked.connect(self.save)
        self.show()
    #функция сохранения заметки
    def save(self):
        global writ
        global last_z
        global pos
        last_z=[]
        last_z.append(self.lineEdit.text()) 
        last_z.append(self.textEdit.toPlainText())
        pos = self.lineEdit.text()
        self.close()
#Калькулятор        
class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('калькуляторр.ui', self)
        #кнопки ввода данных
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
        self.b_plus.clicked.connect(self.run_plus)
        self.b_minus.clicked.connect(self.run_minus)
        self.b_sin.clicked.connect(self.run_sin)
        self.b_cos.clicked.connect(self.run_cos)
        self.b_tg.clicked.connect(self.run_tg)
        self.b_st.clicked.connect(self.run_st)
        self.b_split.clicked.connect(self.run_split)
        self.b_mult.clicked.connect(self.run_mult)
        self.b_log.clicked.connect(self.run_log10)
        self.b_degree.clicked.connect(self.run_degree)
    #функции реализующие нажатие клавиш 
    
    #функция 'равно' вычисляет введенные данные
    def run(self):
        try:
            a = self.str_count.text()
            a=a.replace('^','**')
            a=a.replace('sin(','math.sin(')
            a=a.replace('cos(','math.cos(')
            a=a.replace('tg(','math.tan(')
            a=a.replace('log10(','math.log10(')
            a=a.replace('п','math.pi')
            a=a.replace('e','math.e')
            
            #вычисление подкоренного выражения
            while a.count('√')!=0:
                in_root=a.index('√')
                last_root=a[in_root+1:]
                under_root=''
                for i in last_root:
                    if i.isdigit() or i=='.':
                        under_root+=i
                    else:
                        break
                root=math.sqrt(float(under_root))
                a=a[:in_root]+str(root)+a[in_root+len(under_root)+1:]     
            #вычисление факториала
            while a.count('!')!=0:
                index_mark=a.index('!')
                before_ex_mark=a[:index_mark]
                before_ex_mark=before_ex_mark[::-1]
                in_ex_mark=''
                for i in before_ex_mark:
                    if i.isdigit() or i=='.':
                        in_ex_mark+=i
                    else:
                        break
                in_ex_mark=in_ex_mark[::-1]
                fact=math.factorial(float(in_ex_mark))
                a=a[:index_mark-len(in_ex_mark)]+str(fact)+a[index_mark+1:]
                self.str_count.clear()
            #подсчёт данных
            self.str_count.setText(str(eval(a)))
        #проверка некорретного ввода данных
        except Exception:
            self.str_count.clear()
            self.str_count.setText('Ошибка ввода')
    #функция '1' печатает символ:'1' в строку данных
    def run_1(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '1')
#функция '2' печатает символ:'2' в строку данных
    def run_2(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '2')
#функция '3' печатает символ:'3' в строку данных
    def run_3(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '3')
#функция '4' печатает символ:'4' в строку данных
    def run_4(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '4')
#функция '5' печатает символ:'5' в строку данных
    def run_5(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '5')
#функция '6' печатает символ:'6' в строку данных
    def run_6(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '6')
#функция '7' печатает символ:'7' в строку данных
    def run_7(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '7')
#функция '8' печатает символ:'8' в строку данных
    def run_8(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '8')
#функция '9' печатает символ:'9' в строку данных
    def run_9(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '9')
#функция '0' печатает символ:'0' в строку данных
    def run_0(self):
        a = self.str_count.text()
        if a == '' or (a[-1] != 'п' and a[-1] != 'e'):
            self.str_count.setText(self.str_count.text() + '0')
#функция '(' печатает символ:'(' в строку данных
    def run_left(self):
        if self.str_count.text() == '' or self.str_count.text()[-1] in ['+', '^', '-', '/', '√',
                                                                        '∛']:
            self.str_count.setText(self.str_count.text() + '(')
#функция ')' печатает символ:')' в строку данных
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
#функция '.' печатает символ:'.' в строку данных
    def run_p(self):
        self.str_count.setText(self.str_count.text() + '.')
#функция '<---' убирает последний символ в строке данных

    def run_back(self):
        a = self.str_count.text()
        self.str_count.setText(a[:len(a) - 1])
#функция 'С' удаляет все символы в строке данных
    def run_c(self):
        self.str_count.clear()
#функция 'П' печатает символ:'П' в строку данных
    def run_pi(self):
        a = self.str_count.text()
        if a == '' or a[-1] in ['+', '^', '-', '/', '√', '∛','*']:
            self.str_count.setText(a + 'п')
#функция 'e' печатает символ:'e' в строку данных
    def run_e(self):
        a = self.str_count.text()
        if a == '' or a[-1] in ['+', '^', '-', '/', '√', '∛','*']:
            self.str_count.setText(a + 'e')
#функция '+' печатает символ:'+' в строку данных
    def run_plus(self):
        self.str_count.setText(self.str_count.text() + '+')
#функция '-' печатает символ:'-' в строку данных
    def run_minus(self):
        self.str_count.setText(self.str_count.text() + '-')
#функция '*' печатает символ:'*' в строку данных
    def run_mult(self):
        self.str_count.setText(self.str_count.text() + '*')
#функция '^' печатает символ:'^' в строку данных
    def run_st(self):
        self.str_count.setText(self.str_count.text() + '^')
#функция '/' печатает символ:'/' в строку данных
    def run_split(self):
        self.str_count.setText(self.str_count.text() + '/')
#функция '!' печатает символ:'!' в строку данных
    def run_fact(self):
        self.str_count.setText(self.str_count.text() + '!')
#функция 'синус' печатает символ:'sin(' в строку данных(ввод в радианах)
    def run_sin(self):
        a = self.str_count.text()
        if a == '' or a[-1] in ['+', '^', '-', '/', '√', '∛','*']:
            self.str_count.setText(self.str_count.text() + 'sin(')
#функция 'косинуc' печатает символ:'cos(' в строку данных(ввод в радианах)
    def run_cos(self):
        a = self.str_count.text()
        if a == '' or a[-1] in ['+', '^', '-', '/', '√', '∛','*']:
            self.str_count.setText(self.str_count.text() + 'cos(')
#функция 'тангенс' печатает символ:'tg(' в строку данных(ввод в радианах)
    def run_tg(self):
        a = self.str_count.text()
        if a == '' or a[-1] in ['+', '^', '-', '/', '√', '∛','*']:
            self.str_count.setText(self.str_count.text() + 'tg(')
#функция 'логоритм из 10' печатает символ:'log10(' в строку данных
    def run_log10(self):
        a = self.str_count.text()
        if a == '' or a[-1] in ['+', '^', '-', '/', '√', '∛','*']:
            self.str_count.setText(self.str_count.text() + 'log10(')
#функция 'корень' печатает символ:'√' в строку данных
    def run_root(self):
        a = self.str_count.text()
        self.str_count.setText(self.str_count.text() + '√')
#функция перевода из радиан в градусы, переводит из радиан в градусы
    def run_degree(self):
        a = self.str_count.text()
        try:
            a=math.degrees(int(a))
            self.str_count.clear()
            self.str_count.setText(str(a)+'°') 
        except Exception:
            self.str_count.clear()
            self.str_count.setText('Введите только одно число')        
        
#класс отвечающий за изменения содержания заметки
class Zam_text(QMainWindow):
    #конструктор класса основа дизайна окна
    def __init__(self):
        global writ
        super().__init__()
        uic.loadUi('open_zamet.ui', self)
        self.textEdit.setPlainText(writ[open_z])
        self.save_z.clicked.connect(self.red)
        self.show()
    #функция сохранения изменения содержания заметки
    def red(self):
        global writ
        writ[open_z]=self.textEdit.toPlainText()
        self.close()
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())