#подключение библиотек
from random import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout
app = QApplication([])
main_win =  QWidget()
main_win.show()
#создание элементов интерфейса
title = QLabel("Нажмите что бы узнать победителя")
button = QPushButton('Сгенерировать')
number = QLabel("?")
#привязка элементов к вертикальной линии
v_line = QVBoxLayout()
v_line.addWidget(
    title, alignment = Qt.AlignCenter
)
v_line.addWidget(number, alignment = Qt.AlignCenter)
v_line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(v_line)
#обработка событий
def show_winner():
    title.setText("Победитель:")
    number.setText(str(randint(0,100)))
button.clicked.connect(show_winner)
app.exec_()