from SegundoParcial.simpson import Simpson
import math

class Programa3(object):

    def __init__(self, dof, p, d=0.5, tolerancia=0.00001):
        self.dof = dof
        self.p = p
        self.d = d
        self.tolerancia = tolerancia
        self.resultado = 0

    def gamma(self, x):
        return math.gamma(x)    
    
    def funcion_t(self, x):
        while True:
            simpson = Simpson(x, self.dof)
            simpson.calcular()
            resultado_simpson = simpson.resultado

            if abs(resultado_simpson - self.p) < self.tolerancia:
                return x
            elif resultado_simpson < self.p:
                x += self.d
            else:
                x -= self.d
            
    def calcular(self):
        x = self.funcion_t(self.d)
        self.resultado = x

    def obtener_resultado(self):
        return self.resultado