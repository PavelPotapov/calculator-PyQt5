#from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt 
from random import randint


app = QApplication([])

window = QWidget()
window.resize(300, 400)
window.setWindowIcon(QIcon("log.jpg"))
window.setWindowTitle('Калькулятор V1.0')
window.show()


name = QLabel("Калькулятор V1.0 простой")

input1 = QLineEdit()
input1.setPlaceholderText('введите число')
btn1 = QPushButton('clear') #кнопка очищения input1
error_text1 = QLabel('')
act_btn1 = QPushButton('+')
act_btn2 = QPushButton('-')
act_btn3 = QPushButton('*')
act_btn4 = QPushButton('/')
input2 = QLineEdit()
input2.setPlaceholderText('введите число')
btn2 = QPushButton('clear') #кнопка очищения input1
error_text2 = QLabel('Тут будет текст ошибки, если введут что-то не то')

n1 = QLabel('0')
a = QLabel('')
n2 = QLabel('0')
r = QLabel('Результат')

main_line = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()
row4 = QHBoxLayout()
main_line.addWidget(name)
row1.addWidget(input1)
row1.addWidget(btn1)
main_line.addLayout(row1)
main_line.addWidget(error_text1)
row2.addWidget(act_btn1)
row2.addWidget(act_btn2)
row2.addWidget(act_btn3)
row2.addWidget(act_btn4)
main_line.addLayout(row2)
row3.addWidget(input2)
row3.addWidget(btn2)

row4.addWidget(n1)
row4.addWidget(a)
row4.addWidget(n2)
row4.addWidget(r)

main_line.addLayout(row3)
main_line.addWidget(error_text2)
main_line.addLayout(row4)
window.setLayout(main_line)


num1 = 0
num2 = 0
action = '' #эта переменная нужна для того, чтобы определять тип действия

def result():
    global num1, num2, action
    try:
        if not isinstance(num1, str) and not isinstance(num2, str):
            if action == '+':
                r.setText(str(num1 + num2))
            elif action == '-':
                r.setText(str(num1 - num2))
            elif action == '*':
                r.setText(str(num1 * num2))
            elif action == '/':
                r.setText(str(num1 / num2))
            else:
                r.setText('')
        else:
            r.setText('error')
    except:
        r.setText('error')

def test1():
    global num1
    res = input1.text()
    if len(res) != 0:
        try:
            if '.' in res:
                num1 = float(res)
            else:
                num1 = int(res)
            n1.setText(str(num1))
            error_text1.setText('')
        except:
            num1 = 'error1'
            n1.setText(num1)
            error_text1.setText('Вы ввели что-то не то. Вводите только целые числа')
    else:
        n1.setText('')
        error_text1.setText('')
    result()   
def test2():
    global num2
    res = input2.text()
    if len(res) != 0:
        try:
            if '.' in res:
                num2 = float(res)
            else:
                num2 = int(res)
            n2.setText(str(num2))
            error_text2.setText('')
        except:
            num2 = 'error1'
            n2.setText(num1)
            error_text2.setText('Вы ввели что-то не то. Вводите только целые числа')
    else:
        n2.setText('')
        error_text1.setText('')
    result()

def clear1():
    input1.setText('')
    r.setText('')
    
def clear2(): 
    input2.setText('')
    r.setText('')

def plus():
    global action
    action = "+"
    a.setText(action)
    result()
def minus():
    global action
    action = "-"
    a.setText(action)
    result()
def mult():
    global action
    action = "*"
    a.setText(action)
    result()
def division():
    global action
    action = "/"
    a.setText(action)
    result()

input1.textChanged.connect(test1)
input2.textChanged.connect(test2)
btn1.clicked.connect(clear1)
btn2.clicked.connect(clear2)
act_btn1.clicked.connect(plus)
act_btn2.clicked.connect(minus)
act_btn3.clicked.connect(mult)
act_btn4.clicked.connect(division)
app.exec()