# load/load_ventana_programa4.py
from PyQt5 import QtWidgets, uic
from SegundoParcial.programa4 import AnalisisCompleto
from datos.casos_prog4 import (
    ESTIMATED_PROXY,
    ACTUAL_ADDED_MOD,
    ACTUAL_HOURS,
    XK
)

class VentanaPrograma4(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/programa_4.ui", self)
        self.show()

        self.boton_sumar.clicked.connect(self.caso1)
        self.boton_sumar_2.clicked.connect(self.caso2)

 
    # CASO DE PRUEBA 1
    def caso1(self):
        modelo = AnalisisCompleto(
            ESTIMATED_PROXY,
            ACTUAL_ADDED_MOD,
            XK
        )

        modelo.calcular_correlacion()
        modelo.calcular_significancia()
        modelo.calcular_regresion()
        modelo.calcular_intervalo_prediccion()

        # Valores reales
        self.lineEdit_6.setText("0.954496574")
        self.lineEdit_7.setText("0.91106371")
        self.lineEdit_8.setText("1.77517E-05")
        self.lineEdit_9.setText("-22.55253275")
        self.lineEdit_10.setText("1.727932426")
        self.lineEdit_11.setText("644.4293838")
        self.lineEdit_12.setText("230.0017197")
        self.lineEdit_13.setText("874.4311035")
        self.lineEdit_14.setText("414.427664")

        # Valores actuales
        self.lineEdit.setText(str(round(modelo.r, 9)))
        self.lineEdit_2.setText(str(round(modelo.r2, 9)))
        self.lineEdit_3.setText("{:.5E}".format(modelo.tail_area))
        self.lineEdit_4.setText(str(round(modelo.b0, 8)))
        self.lineEdit_5.setText(str(round(modelo.b1, 9)))
        self.lineEdit_15.setText(str(round(modelo.yk, 7)))
        self.lineEdit_16.setText(str(round(modelo.range70, 7)))
        self.lineEdit_17.setText(str(round(modelo.upi, 7)))
        self.lineEdit_18.setText(str(round(modelo.lpi, 7)))

    
    # CASO DE PRUEBA 2
    def caso2(self):
        modelo = AnalisisCompleto(
            ESTIMATED_PROXY,
            ACTUAL_HOURS,
            XK
        )

        modelo.calcular_correlacion()
        modelo.calcular_significancia()
        modelo.calcular_regresion()
        modelo.calcular_intervalo_prediccion()

        # Valores reales
        self.lineEdit_6.setText("0.933306898")
        self.lineEdit_7.setText("0.871061766")
        self.lineEdit_8.setText("7.98203E-05")
        self.lineEdit_9.setText("-4.038881575")
        self.lineEdit_10.setText("0.16812665")
        self.lineEdit_11.setText("60.85800528")
        self.lineEdit_12.setText("27.55764748")
        self.lineEdit_13.setText("88.41565276")
        self.lineEdit_14.setText("33.3003578")

        # Valores actuales
        self.lineEdit.setText(str(round(modelo.r, 9)))
        self.lineEdit_2.setText(str(round(modelo.r2, 9)))
        self.lineEdit_3.setText("{:.5E}".format(modelo.tail_area))
        self.lineEdit_4.setText(str(round(modelo.b0, 8)))
        self.lineEdit_5.setText(str(round(modelo.b1, 8)))
        self.lineEdit_15.setText(str(round(modelo.yk, 8)))
        self.lineEdit_16.setText(str(round(modelo.range70, 8)))
        self.lineEdit_17.setText(str(round(modelo.upi, 8)))
        self.lineEdit_18.setText(str(round(modelo.lpi, 8)))