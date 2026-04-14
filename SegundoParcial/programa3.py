from SegundoParcial.simpson import Simpson
import math

class IntegracionInversa(object):

    def __init__(self, p, dof, error=0.000001):
        self.p = p
        self.dof = dof
        self.error = error

        self.x = 1.0     # valor inicial
        self.d = 0.5     # incremento inicial
        self.resultado = 0

    def calcular(self):
        signo_anterior = None
        max_iter = 10000   # límite de iteraciones
        iter_count = 0

        while iter_count < max_iter:
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

            # Si d se vuelve demasiado pequeño, detener
            if self.d < 1e-10:
                self.resultado = self.x
                break

            iter_count += 1

        # Si se alcanzó el máximo de iteraciones sin converger
        if iter_count == max_iter:
            self.resultado = self.x
