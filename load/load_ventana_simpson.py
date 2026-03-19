from PyQt5 import QtWidgets, uic
from SegundoParcial.simpson import Simpson

class VentanaSimpson(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/programa_2.ui", self)
        self.show()

        # Conectar botón
        self.boton_sumar.clicked.connect(self.calcularIntegral)

    def calcularIntegral(self):
            # Leer datos de entrada
            x = float(self.edit_numero1.text())
            dof = int(self.edit_numero1_2.text())

            # Crear objeto de integración
            integracion = Simpson(x, dof)
            integracion.calcular()

            # Mostrar resultado
            self.edit_numero1_3.setText(str(round(integracion.resultado, 5)))