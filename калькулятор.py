from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMainWindow, QComboBox, QHBoxLayout, QLineEdit, QPushButton

money = {"USD" : 1,
    "EUR" : 1.1,
       "UAH" : 0.03}
app = QApplication([])
mw = QWidget()
mw.setWindowTitle("canvertor")
mw.resize(600, 500)
qw = QLabel("Type of money")
qw1 = QLabel("Type of money")
cb1 = QComboBox()
cb1.addItems(money.keys())
cb2= QComboBox()
cb2.addItems(money.keys())
LE = QLineEdit()
btn = QPushButton("ПОЛОМАТЬ ТВОЙ ГАДЖЕТ")
lm = QVBoxLayout()
lm1 = QHBoxLayout()
lm2 = QHBoxLayout()
lm3 = QHBoxLayout()
lm4 = QHBoxLayout()
lm1.addWidget(qw, alignment = Qt.AlignCenter)
lm1.addWidget(qw1, alignment = Qt.AlignCenter)
lm2.addWidget(cb1, alignment = Qt.AlignCenter)
lm2.addWidget(cb2, alignment = Qt.AlignCenter)
lm3.addWidget(LE, alignment = Qt.AlignCenter)
lm4.addWidget(btn, alignment = Qt.AlignCenter)
lm.addLayout(lm1)
lm.addLayout(lm2)
lm.addLayout(lm3)
lm.addLayout(lm4)


mw.setLayout(lm)
mw.show()
app.exec_()

