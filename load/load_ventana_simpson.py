# load/load_ventana_integracion.py
from PyQt5 import QtWidgets, uic
from SegundoParcial import Simpson
from datos.casos_pruebas import CASOS_INTEGRACION

class VentanaSimpson(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_integracion.ui", self)
        self.show()

        self.btnCaso1.clicked.connect(lambda: self.ejecutarCaso(1))
        self.btnCaso2.clicked.connect(lambda: self.ejecutarCaso(2))
        self.btnCaso3.clicked.connect(lambda: self.ejecutarCaso(3))

    def ejecutarCaso(self, caso):
        datos = CASOS_INTEGRACION[caso]

        integracion = IntegracionSimpson(
            datos["x"],
            datos["dof"]
        )
        integracion.calcular()

        # Mostrar resultado calculado
        self.lblResultado.setText(str(round(integracion.resultado, 5)))

        # Mostrar valor esperado
        self.lblEsperado.setText(str(datos["esperado"]))