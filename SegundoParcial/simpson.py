import numpy as np
from scipy.special import gamma

class Simpson(object):

    def __init__(self, x, dof, n=1000):
        self.x = x
        self.dof = dof
        self.n = n if n % 2 == 0 else n + 1  # n debe ser par
        self.resultado = 0

    def gamma(self, x):
        return math.gamma(x)

    def funcion_t(self, x):
        num = self.gamma((self.dof + 1) / 2)
        den = math.sqrt(self.dof * math.pi) * self.gamma(self.dof / 2)
        base = 1 + (x**2 / self.dof)
        exp = - (self.dof + 1) / 2
        return (num / den) * (base ** exp)

    def calcular(self):
        a = 0
        b = self.x
        h = (b - a) / self.n

        suma = self.funcion_t(a) + self.funcion_t(b)

        for i in range(1, self.n):
            x_i = a + i * h
            if i % 2 == 0:
                suma += 2 * self.funcion_t(x_i)
            else:
                suma += 4 * self.funcion_t(x_i)

        self.resultado = (h / 3) * suma