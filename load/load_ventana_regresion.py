# load/load_ventana_regresion.py
from PyQt5 import QtWidgets, uic
from SegundoParcial.regreli import RegresionLineal
from datos.casos_pruebar import *

class VentanaRegresion(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_regresion.ui", self)
        self.show()

        self.btnCaso1.clicked.connect(lambda: self.ejecutarCaso(1))
        self.btnCaso2.clicked.connect(lambda: self.ejecutarCaso(2))
        self.btnCaso3.clicked.connect(lambda: self.ejecutarCaso(3))
        self.btnCaso4.clicked.connect(lambda: self.ejecutarCaso(4))

    def ejecutarCaso(self, caso):
        if caso == 1:
            x, y = ESTIMATED_PROXY, ACTUAL_ADDED_MOD
        elif caso == 2:
            x, y = ESTIMATED_PROXY, ACTUAL_HOURS
        elif caso == 3:
            x, y = PLAN_ADDED_MOD, ACTUAL_ADDED_MOD
        else:
            x, y = PLAN_ADDED_MOD, ACTUAL_HOURS

        modelo = RegresionLineal(x, y)
        modelo.calcular(XK)

        # Mostrar resultados actuales
        self.lblB0.setText(str(round(modelo.b0, 4)))
        self.lblB1.setText(str(round(modelo.b1, 6)))
        self.lblR.setText(str(round(modelo.r, 4)))
        self.lblR2.setText(str(round(modelo.r2, 4)))
        self.lblYk.setText(str(round(modelo.yk, 4)))

        # Mostrar resultados esperados
        esperado = CASOS_ESPERADOS[caso]
        self.lblExpB0.setText(str(esperado["b0"]))
        self.lblExpB1.setText(str(esperado["b1"]))
        self.lblExpR.setText(str(esperado["r"]))
        self.lblExpR2.setText(str(esperado["r2"]))
        self.lblExpYk.setText(str(esperado["yk"]))
