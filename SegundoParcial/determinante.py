import math
class Determinante3x3:

    def __init__(self, A):
        self.A = A

    def calcular(self):
        a,b,c = self.A[0]
        d,e,f = self.A[1]
        g,h,i = self.A[2]
        return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)