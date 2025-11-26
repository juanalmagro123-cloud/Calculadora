from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.uic import loadUi
from view.Calculadora import Calculadora


if __name__ == "__main__":
    app = QApplication([])
    tela = Calculadora()
    app.exec_()

   

