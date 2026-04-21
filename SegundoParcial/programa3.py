from SegundoParcial.simpson import Simpson
import math

class IntegracionInversa(object):

    def __init__(self, p, dof, error=0.000001):
        self.p = p
        self.dof = dof
        self.error = error

        self.x = 1.0     
        self.d = 0.5     
        self.resultado = 0

    def calcular(self):
        signo_anterior = None
        max_iter = 10000  
        iter_count = 0

        while iter_count < max_iter:
            integracion = Simpson(self.x, self.dof)
            integracion.calcular()
            valor_actual = integracion.resultado

            diferencia = valor_actual - self.p

            
            if abs(diferencia) < self.error:
                self.resultado = self.x
                break

            signo_actual = diferencia > 0

          
            if diferencia < 0:
                self.x += self.d
            else:
                self.x -= self.d

            
            if signo_anterior is not None and signo_actual != signo_anterior:
                self.d /= 2

            signo_anterior = signo_actual

            
            if self.x < 0:
                self.x = 0

           
            if self.d < 1e-10:
                self.resultado = self.x
                break

            iter_count += 1

      
        if iter_count == max_iter:
            self.resultado = self.x
