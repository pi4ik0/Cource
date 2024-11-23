from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QMessageBox, QRadioButton

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Ютуб-канал Crazy People хоче зробити окремий міні-конкурс для спонсорів каналу')
question = QLabel('Як звали першого ютуб-блогера, який набрав 100000000 підписників?')
btn_answer1 = QRadioButton('PewDiePie')
btn_answer2 = QRadioButton('Рет і Лінк')
btn_answer3 = QRadioButton('SlivkiShow')
btn_answer4 = QRadioButton('TheBrianMaps')
btn_answer5 = QRadioButton('Mister Max')
btn_answer6 = QRadioButton('EeOneGuy')
layout_main = QVBoxLayout()
lm1 = QHBoxLayout()
lm2 = QHBoxLayout()
lm3 = QHBoxLayout()
layout_main.addWidget(question, alignment = Qt.AlignCenter)
lm1.addWidget(btn_answer1, alignment = Qt.AlignCenter)
lm1.addWidget(btn_answer2, alignment = Qt.AlignCenter)
lm2.addWidget(btn_answer3, alignment = Qt.AlignCenter)
lm2.addWidget(btn_answer4, alignment = Qt.AlignCenter)
lm3.addWidget(btn_answer5, alignment = Qt.AlignCenter)
lm3.addWidget(btn_answer6, alignment = Qt.AlignCenter)
layout_main.addLayout(lm1)
layout_main.addLayout(lm2)
layout_main.addLayout(lm3)


def show_win():
    btn_answer1.clicked.connect(show_win)


def victory_win():
    victory_win = QMessageBox()
    victory_win.setText('Правильно! Ви виграли гіроскутер')
    victory_win.exec_()

def lose():
    lose = QMessageBox()
    lose.setText('Ні, PewDiePie. Ви виграли фірмовий плакат')
    lose.exec_()

btn_answer1.clicked.connect(victory_win)
btn_answer2.clicked.connect(lose)
btn_answer3.clicked.connect(lose)
btn_answer4.clicked.connect(lose)
btn_answer5.clicked.connect(lose)
btn_answer6.clicked.connect(lose)

main_win.setLayout(layout_main)
main_win.show()
app.exec_()