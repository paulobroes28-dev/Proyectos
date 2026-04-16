import math
import numpy as np
from SegundoParcial.regreli import RegresionLineal
from SegundoParcial.simpson import Simpson
from SegundoParcial.programa3 import IntegracionInversa

class AnalisisCompleto(object):

    def __init__(self, x, y, xk):
        self.x = np.array(x)
        self.y = np.array(y)
        self.xk = xk
        self.n = len(x)
        self.r = 0
        self.r2 = 0
        self.b0 = 0
        self.b1 = 0
        self.yk = 0
        self.tail_area = 0
        self.range70 = 0
        self.upi = 0
        self.lpi = 0


    def calcular_correlacion(self):
        self.r = np.corrcoef(self.x, self.y)[0,1]
        self.r2 = self.r ** 2


    def calcular_significancia(self):
        dof = self.n - 2
        x_t = abs(self.r) * np.sqrt(dof / (1 - self.r2))
        integracion = Simpson(x_t, dof)
        integracion.calcular()
        p = integracion.resultado
        self.tail_area = 1 - (2 * p)


    def calcular_regresion(self):
        xm = np.mean(self.x)
        ym = np.mean(self.y)

        self.b1 = np.sum((self.x - xm)*(self.y - ym)) / np.sum((self.x - xm)**2)
        self.b0 = ym - self.b1 * xm
        self.yk = self.b0 + self.b1 * self.xk


    def calcular_intervalo_prediccion(self):
        dof = self.n - 2
        t_inv = IntegracionInversa(0.35, dof)
        t_inv.calcular()
        t = t_inv.resultado
        s = np.sqrt(
            np.sum((self.y - (self.b0 + self.b1*self.x))**2) / dof
        )
        term = np.sqrt(
            1 + (1/self.n) + ((self.xk - np.mean(self.x))**2 / np.sum((self.x - np.mean(self.x))**2))
        )
        self.range70 = t * s * term
        self.upi = self.yk + self.range70
        self.lpi = self.yk - self.range70