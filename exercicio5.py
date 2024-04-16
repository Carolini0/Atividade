import math  

class triangulo:
    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro (self):
        return self.lado1 + self.lado2 + self.lado3
    
    def calcular_area (self):

        s= self.calcular_perimetro()/2
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return area 
    
if __name__=="__main__":
    triangulo = triangulo(2, 3, 4)
    print ("Perímetro:", triangulo.calcular_perimetro())
    print ("triangulo:",  triangulo.calcular_area())
   