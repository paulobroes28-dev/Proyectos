import numpy as np
from scipy.special import gamma

class Simpson(object):

    def __init__(self, f, a, b, n):
        self.f = f
        self.a = a
        self.b = b
        self.n = n

    def calcular(self):
        h = (self.b - self.a) / self.n

        sum_odd = 0
        sum_even = 0

        for i in range(1, self.n):
            x_i = self.a + i * h
            if i % 2 == 0:
                sum_even += self.f(x_i)
            else:
                sum_odd += self.f(x_i)

        integral = (h / 3) * (self.f(self.a) + 4 * sum_odd + 2 * sum_even + self.f(self.b))
        return integral


