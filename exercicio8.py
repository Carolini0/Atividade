'''
8-Crie uma classe Retângulo com atributos para altura e largura. 
Adicione métodos para calcular a área e o perímetro do retângulo.

'''
# DECLARANDO A CLASSE:
class Retangulo:
    # CRIANDO FUNÇÃO NA CLASSE
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura

    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def calcular_area(self):
        return f'A area do retângulo é: {self.altura * self.largura}'
    
    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def perimetro(self):
        return f'O perimetro do retângulo é: {self.altura + self.altura + self.largura + self.largura}'

# DECLARANDO VALORES PARA A FUNÇÃO DA CLASSE
if __name__=='__main__':
    valores1 = Retangulo(4,6)
    valores2 = Retangulo(9,7)

    # PRINTANDO E CONCECTANDO TODAS AS AÇÕES DOS VALORES
    print(valores1.calcular_area())

    print(valores2.calcular_area())

    print(valores1.perimetro())
    
    print(valores2.perimetro())
