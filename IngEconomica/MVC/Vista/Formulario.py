import sys
from PyQt5 import QtWidgets, uic
from IngEconomica.MVC.Controlador.Botones import Controlador
from IngEconomica.MVC.Modelo.Conexion import Database

qtCreatorFile = "Formulario.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = Database()
        self.controlador = Controlador(self, self.db)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
