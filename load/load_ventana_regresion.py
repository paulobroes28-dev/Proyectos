# load/load_ventana_regresion.py
from PyQt5 import QtWidgets, uic
from SegundoParcial.regreli import RegresionLineal
from datos.casos_pruebar import *

class VentanaRegresion(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/programa_1.ui", self)
        self.show()

        self.boton_sumar.clicked.connect(lambda: self.ejecutarCaso(1))
        self.boton_sumar_2.clicked.connect(lambda: self.ejecutarCaso(2))
        self.boton_sumar_3.clicked.connect(lambda: self.ejecutarCaso(3))
        self.boton_sumar_4.clicked.connect(lambda: self.ejecutarCaso(4))

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
        self.lineEdit.setText(str(round(modelo.b0, 4)))
        self.lineEdit_2.setText(str(round(modelo.b1, 6)))
        self.lineEdit_3.setText(str(round(modelo.r, 4)))
        self.lineEdit_4.setText(str(round(modelo.r2, 4)))
        self.lineEdit_5.setText(str(round(modelo.yk, 4)))

        # Mostrar resultados esperados
        esperado = CASOS_ESPERADOS[caso]
        self.lineEdit_6.setText(str(esperado["b0"]))
        self.lineEdit_7.setText(str(esperado["b1"]))
        self.lineEdit_8.setText(str(esperado["r"]))
        self.lineEdit_9.setText(str(esperado["r2"]))
        self.lineEdit_10.setText(str(esperado["yk"]))
