from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.uic import loadUi
from PyQt5.QtGui import QKeySequence
from funcoes import soma


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
        self.btn_po.clicked.connect(self.addComma)             
        
    def addComma(self):
        visor = self.tela.text()
        self.tela.setText(str(visor)+",")
        

    def addNumber (self, numero):
        visor = self.tela.text()
        self.tela.setText(str(visor)+str(numero))

    def setOperationDisplay(self, operation):
        self.tela.setText(operation)
    def getNumberDisplay(self, display):
        number = display.text()
        number = number.replace(",", ".")
        return float(number)
    def setCalcDisplay(self, num1, num2, operation):
        num1 = str(num1)
        num2 = str(num2)
        num1 = num1.replace(".", ",")
        num2 = num2.replace(".", ",")
        self.tela_2.setText(f"{num1} {operation} {num2}")

    
    

    def setNumberDisplay(self, number):
        number = str(number)
        number = number.replace(".", ",")
        self.tela.setText(number)

    def showResult(self):
        num1 = self.getNumberDisplay(self.tela_2)
        num2 = self.getNumberDisplay(self.tela)

        result = soma(num1, num2)
        self.setNumberDisplay(result)
        self.setCalcDisplay(num1, num2, "+")

    

