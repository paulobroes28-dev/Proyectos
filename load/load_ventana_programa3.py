from PyQt5 import QtWidgets, uic
from SegundoParcial.programa3 import IntegracionInversa

class VentanaIntegracionInversa(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/programa_3.ui", self)
        self.show()

        self.boton_sumar.clicked.connect(self.calcularX)

    def calcularX(self):
        try:
            p = float(self.edit_numero1.text())
            dof = int(self.edit_numero1_2.text())

            inversa = IntegracionInversa(p, dof)
            inversa.calcular()

            self.edit_numero1_3.setText(str(round(inversa.resultado, 5)))

        except ValueError:
            QtWidgets.QMessageBox.warning(
                self,
                "Error",
                "Ingrese valores válidos para p y dof"
            )