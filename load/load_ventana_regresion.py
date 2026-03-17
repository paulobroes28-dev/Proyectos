# load/load_ventana_regresion.py
from PyQt5 import QtWidgets, uic
from SegundoParcial.regreli import RegresionLineal
from datos.casos_prueba import *

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





        # datos/casos_prueba.py

# Datos base
ESTIMATED_PROXY = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]

ACTUAL_ADDED_MOD = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
ACTUAL_HOURS = [15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]

#PLAN_ADDED_MOD  = [163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130]


XK = 386

# Valores esperados
CASOS_ESPERADOS = {
    1: {"b0": -22.55, "b1": 1.7279, "r": 0.9545, "r2": 0.9111, "yk": 644.429},
    2: {"b0": -4.039, "b1": 0.1681, "r": 0.9333, "r2": 0.8711, "yk": 60.858},
    3: {"b0": -23.92, "b1": 1.43097, "r": 0.9631, "r2": 0.9276, "yk": 528.4294},
    4: {"b0": -4.604, "b1": 0.140164, "r": 0.9480, "r2": 0.8988, "yk": 49.4994}
}