from PyQt5 import QtWidgets, uic
from SegundoParcial.programa4 import Programa4

class Ventana(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/programa_4.ui", self)
        self.show()