from PyQt5 import QtWidgets, uic
from load.load_ventana_regresion import VentanaRegresion
from load.load_ventana_simpson import VentanaSimpson
from load.load_ventana_programa3 import VentanaIntegracionInversa
from load.load_ventana_programa4 import VentanaPrograma4
from load.load_ventana_parabolas import VentanaParabola
from load.load_ventana_elipses import VentanaElipse
from load.load_ventana_determinantes import VentanaDeterminante

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/menu_principal.ui", self)
        self.showMaximized()

        self.actionRegresi_n_Lineal.triggered.connect(self.abrirRegresion)
        self.actionIntegraci_n_Num_rica.triggered.connect(self.abrirIntegracion)
        self.actionIntegraci_n_Inversa.triggered.connect(self.abrirPrograma3)
        self.actionAn_lisis_Completo.triggered.connect(self.abrirPrograma4)
        self.actionPar_bolas.triggered.connect(self.abrirParabola)
        self.actionElipses.triggered.connect(self.abrirElipse)
        self.actionDeterminante_3x3_Sarrus.triggered.connect(self.abrirDeterminante)
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
    
    def abrirPrograma4(self):
        ventana = VentanaPrograma4()
        ventana.exec()

    def abrirParabola(self):
        ventana = VentanaParabola()
        ventana.exec()
    
    def abrirElipse(self):
        ventana = VentanaElipse()
        ventana.exec()

    def abrirDeterminante(self):
        ventana = VentanaDeterminante()
        ventana.exec()

    def salir(self):
        self.close()