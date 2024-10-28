import math

class Calculadora:

    def suma(self, a, b):
        return a + b
    
    def resta(self, a, b):
        return a - b
    
    def multiplicacion(self, a, b):
        return a * b
    
    def division (self, a, b):
        if b != 0:
            return a / b
        
        else:
            return "Error: No se puede dividir por cero"
        
    def porcentaje(self, a, b):
        return (a * b) / 100
    
    def raiz_cuadrada(self, a):
        return math.sqrt(a)