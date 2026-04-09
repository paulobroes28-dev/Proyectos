from SegundoParcial.simpson import Simpson
import math

# clases/integracion_inversa.py
class IntegracionInversa(object):

    def __init__(self, p, dof, error=0.00001):
        self.p = p
        self.dof = dof
        self.error = error

        self.x = 1.0     # valor inicial
        self.d = 0.5     # incremento inicial
        self.resultado = 0

    def calcular(self):
        signo_anterior = None

        while True:
            integracion = Simpson(self.x, self.dof)
            integracion.calcular()
            valor_actual = integracion.resultado

            diferencia = valor_actual - self.p

            # ¿Ya es suficientemente cercano?
            if abs(diferencia) < self.error:
                self.resultado = self.x
                break

            signo_actual = diferencia > 0

            # Ajustar x
            if diferencia < 0:
                self.x += self.d
            else:
                self.x -= self.d

            # Ajustar d si cambia el signo
            if signo_anterior is not None and signo_actual != signo_anterior:
                self.d /= 2

            signo_anterior = signo_actual

            # Evitar x negativo
            if self.x < 0:
                self.x = 0