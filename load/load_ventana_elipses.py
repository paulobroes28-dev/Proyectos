from PyQt5 import QtWidgets, uic
from SegundoParcial.elipses import Elipses

class VentanaElipse(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/elipse.ui", self)
        self.boton_sumar.clicked.connect(self.calcular)

    def calcular(self):
        a = float(self.edit_numero1.text())
        b = float(self.edit_numero1_2.text())

        e = Elipses(a, b)

        self.edit_numero1_6.setText(e.orientacion())
        self.edit_numero1_5.setText(str(e.eje_mayor()))
        self.edit_numero1_4.setText(str(e.eje_menor()))
        self.edit_numero1_8.setText(str(e.vertices()))
        self.edit_numero1_7.setText(str(e.co_vertices()))
        self.edit_numero1_9.setText(str(e.focos()))
        self.edit_numero1_3.setText(str(e.excentricidad()))