import math

class Elipses:

    def __init__(self, a, b, h=0, k=0):
        self.a = a
        self.b = b
        self.h = h
        self.k = k

    def orientacion(self):
        return "Horizontal" if self.a > self.b else "Vertical"

    def eje_mayor(self):
        return 2*max(self.a, self.b)

    def eje_menor(self):
        return 2*min(self.a, self.b)

    def c(self):
        return math.sqrt(abs(self.a**2 - self.b**2))

    def focos(self):
        c = self.c()
        if self.orientacion() == "Horizontal":
            return (self.h - c, self.k), (self.h + c, self.k)
        else:
            return (self.h, self.k - c), (self.h, self.k + c)

    def vertices(self):
        if self.orientacion() == "Horizontal":
            return (self.h - self.a, self.k), (self.h + self.a, self.k)
        else:
            return (self.h, self.k - self.b), (self.h, self.k + self.b)

    def co_vertices(self):
        if self.orientacion() == "Horizontal":
            return (self.h, self.k - self.b), (self.h, self.k + self.b)
        else:
            return (self.h - self.a, self.k), (self.h + self.a, self.k)

    def excentricidad(self):
        return round(self.c() / max(self.a, self.b), 4)