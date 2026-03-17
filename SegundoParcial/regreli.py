import math

class RegresionLineal(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)

        self.b0 = 0
        self.b1 = 0
        self.r = 0
        self.r2 = 0
        self.yk = 0

    def calcular(self, xk):
        x_prom = sum(self.x) / self.n
        y_prom = sum(self.y) / self.n

        sxy = 0
        sxx = 0
        syy = 0

        for i in range(self.n):
            sxy += (self.x[i] - x_prom) * (self.y[i] - y_prom)
            sxx += (self.x[i] - x_prom) ** 2
            syy += (self.y[i] - y_prom) ** 2

        self.b1 = sxy / sxx
        self.b0 = y_prom - self.b1 * x_prom

        self.r = sxy / math.sqrt(sxx * syy)
        self.r2 = self.r ** 2

        self.yk = self.b0 + self.b1 * xk