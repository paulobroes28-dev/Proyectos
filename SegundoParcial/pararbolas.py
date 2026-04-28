import math

class Parabolas:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def intersecciones_x(self):
        d = self.b**2 - 4*self.a*self.c
        if d < 0:
            return None
        x1 = (-self.b + math.sqrt(d)) / (2*self.a)
        x2 = (-self.b - math.sqrt(d)) / (2*self.a)
        return x1, x2

    def vertice(self):
        h = -self.b / (2*self.a)
        k = self.a*h**2 + self.b*h + self.c
        return h, k

    def apertura(self):
        return "Arriba" if self.a > 0 else "Abajo"

    def parametro_p(self):
        return 1 / (4*self.a)

    def foco(self):
        h, k = self.vertice()
        return h, k + self.parametro_p()

    def directriz(self):
        _, k = self.vertice()
        return k - self.parametro_p()