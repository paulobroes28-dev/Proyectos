from PyQt5 import QtWidgets, uic
from load.load_ventana_regresion import VentanaRegresion
from load.load_ventana_simpson import VentanaSimpson
from load.load_ventana_programa3 import VentanaIntegracionInversa

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/menu_principal.ui", self)
        self.showMaximized()

        self.actionRegresi_n_Lineal.triggered.connect(self.abrirRegresion)
        self.actionIntegraci_n_Num_rica.triggered.connect(self.abrirIntegracion)
        self.actionIntegraci_n_Inversa.triggered.connect(self.abrirPrograma3)
        self.actionSalir.triggered.connect(self.salir)

    def abrirRegresion(self):
        ventana = VentanaRegresion()
        ventana.exec()

    def abrirIntegracion(self):
        ventana = VentanaSimpson()
        ventana.exec()
 
    def abrirPrograma3(self):
        ventana = VentanaIntegracionInversa()
        ventana.exec()

    def salir(self):
        self.close()