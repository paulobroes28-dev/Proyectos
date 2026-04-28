from SegundoParcial.pararbolas import Parabolas
from PyQt5 import QtWidgets, uic

class VentanaParabola(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/parabola.ui", self)
        self.boton_sumar.clicked.connect(self.calcular)

    def calcular(self):
        a = float(self.edit_numero1.text())
        b = float(self.edit_numero1_2.text())
        c = float(self.edit_numero1_3.text())

        p = Parabolas(a, b, c)

        self.edit_numero1_6.setText(p.apertura())
        self.edit_numero1_5.setText(str(p.vertice()))
        self.edit_numero1_7.setText(str(round(p.parametro_p(), 4)))
        self.edit_numero1_4.setText(str(p.foco()))
        self.edit_numero1_8.setText(str(p.directriz()))

        inter = p.intersecciones_x()
        self.edit_numero1_9.setText(str(inter) if inter else "No reales")
