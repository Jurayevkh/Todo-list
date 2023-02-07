from concurrent.futures import thread
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QListWidget,QLabel
from PyQt5.QtGui import QFont

app=QApplication([])
screen=QWidget()
screen.setStyleSheet("background-color:#505050;")
screen.setWindowTitle("To Do List")
# screen.setFixedSize(820,294)

def clear_btn():
    todo3.clear()
    lst.clear()

def add():
    a=0
    if enter.text() and enter.text() not in lst:
        todo.clear()
        lst.append(enter.text())
        for i in range(len(lst)-1, -1, -1):
            todo.addItem((str(a+1)+")" + lst[a]))
            a+=1
    enter.clear()

def do():
    todo2.addItem(todo.currentItem().text())
    todo.takeItem(todo.currentRow())

def ended():
    todo3.addItem(todo2.currentItem().text())
    todo2.takeItem(todo2.currentRow())

lst=[]
first_hor=QHBoxLayout()
second_hor=QHBoxLayout()

first_ver=QVBoxLayout()
second_ver=QVBoxLayout()
third_ver=QVBoxLayout()

send=QPushButton("+",screen)
send.setFixedSize(30,30)
send.setStyleSheet("background-color:darkorange; color:white; border-radius:15px;")
send.clicked.connect(add)

enter=QLineEdit(screen)
enter.setStyleSheet("color:white; border:1px solid white; border-radius:10px;")

todo=QListWidget(screen)
todo.setStyleSheet("background-color:white; border:3px solid black; color:black; border-radius:10px;")
todo.clicked.connect(do)


label2=QLabel("Bajarilmoqda")
label2.setFont(QFont("Gill Sans",31))
label2.setStyleSheet("color:white;")

todo2=QListWidget(screen)
todo2.setStyleSheet("background-color:white; border:3px solid black; color:black; border-radius:10px;")
todo2.clicked.connect(ended)

label3=QLabel("Tugatildi")
label3.setFont(QFont("Gill Sans",31))
label3.setStyleSheet("color:white;")

todo3=QListWidget(screen)
todo3.setStyleSheet("background-color:white; border:3px solid black; color:black; border-radius:10px;")
# todo3.setFixedSize(259,219)

btn_clear=QPushButton("Clear",screen)
btn_clear.setStyleSheet("background-color:darkorange; color:white; border-radius:15px;")
btn_clear.setFixedSize(87,45)
btn_clear.clicked.connect(clear_btn)

first_hor.addWidget(enter)
first_hor.addWidget(send)

first_ver.addLayout(first_hor)
first_ver.addWidget(todo)


second_ver.addWidget(label2)
second_ver.addWidget(todo2)

third_ver.addWidget(label3)
third_ver.addWidget(todo3)
third_ver.addWidget(btn_clear)

second_hor.addLayout(first_ver)
second_hor.addLayout(second_ver)
second_hor.addLayout(third_ver)

screen.setLayout(second_hor)

screen.show()
app.exec_()