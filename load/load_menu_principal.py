from PyQt5 import QtWidgets, uic
from load.load_ventana_regresion import VentanaRegresion
from load.load_ventana_simpson import VentanaSimpson

class MenuPrincipal(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/menu_principal.ui", self)
        self.showMaximized()

        self.actionRegresionLineal.triggered.connect(self.abrirRegresion)
        self.actionSimpson.triggered.connect(self.abrirSimpson)
        self.actionSalir.triggered.connect(self.close)

    def abrirRegresion(self):
        ventana = VentanaRegresion()
        ventana.exec()

    def abrirIntegracion(self):
        ventana = VentanaSimpson()
        ventana.exec()