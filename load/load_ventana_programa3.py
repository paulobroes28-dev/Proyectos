from PyQt5 import QtWidgets, uic
from SegundoParcial.programa3 import Programa3

class VentanaPrograma3(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/programa_3.ui", self)
        self.show()

        # Conectar botón
        self.boton_sumar.clicked.connect(self.calcularIntegral)

    def calcularIntegral(self):
            # Leer datos de entrada
            dof = int(self.edit_numero1.text())
            p = float(self.edit_numero1_2.text())
