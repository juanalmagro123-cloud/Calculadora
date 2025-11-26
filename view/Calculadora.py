from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.uic import loadUi
from PyQt5.QtGui import QKeySequence


class Calculadora(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("view/calculadora.ui", self)
        
        self.show()

        self.btn_0.clicked.connect(lambda: self.addNumber(0))
        self.btn_1.clicked.connect(lambda: self.addNumber(1))
        self.btn_2.clicked.connect(lambda: self.addNumber(2))
        self.btn_3.clicked.connect(lambda: self.addNumber(3))
        self.btn_4.clicked.connect(lambda: self.addNumber(4))
        self.btn_5.clicked.connect(lambda: self.addNumber(5))
        self.btn_6.clicked.connect(lambda: self.addNumber(6))
        self.btn_7.clicked.connect(lambda: self.addNumber(7))
        self.btn_8.clicked.connect(lambda: self.addNumber(8))
        self.btn_9.clicked.connect(lambda: self.addNumber(9))
        self.btn_s.clicked.connect(lambda: self.addNumber("+"))
        self.btn_d.clicked.connect(lambda: self.addNumber("/"))
        self.btn_m.clicked.connect(lambda: self.addNumber("x"))
        self.btn_sb.clicked.connect(lambda: self.addNumber("-"))
        
        
        

    def addNumber (self, numero):
        visor = self.tela.text()
        self.tela.setText(str(visor)+str(numero))

