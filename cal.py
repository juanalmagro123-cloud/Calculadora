import sys
from PyQt5.QtWidgets import QApplication
from view.Calculadora import Calculadora


if __name__ == "__main__":
    app = QApplication([])
    tela = Calculadora()
    sys.exit(app.exec_())

   

