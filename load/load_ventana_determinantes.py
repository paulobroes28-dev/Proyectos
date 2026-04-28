from PyQt5 import QtWidgets, uic
from SegundoParcial.determinante import Determinante3x3

class VentanaDeterminante(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/determinante.ui", self)
        self.boton_sumar.clicked.connect(self.calcular)

    def calcular(self):
        A = [
            [float(self.edit_numero1_2.text()), float(self.edit_numero1_7.text()), float(self.edit_numero1_10.text())],
            [float(self.edit_numero1_3.text()), float(self.edit_numero1_5.text()), float(self.edit_numero1_8.text())],
            [float(self.edit_numero1_4.text()), float(self.edit_numero1_6.text()), float(self.edit_numero1_9.text())]
        ]

        det = Determinante3x3(A).calcular()
        self.edit_numero1.setText(str(det))




            #[float(self.edit_numero1_2.text()), float(self.edit_numero1_3.text()), float(self.edit_numero1_4.text())],
            #[float(self.edit_numero1_7.text()), float(self.edit_numero1_5.text()), float(self.edit_numero1_6.text())],
            #[float(self.edit_numero1_10.text()), float(self.edit_numero1_8.text()), float(self.edit_numero1_9.text())]
 