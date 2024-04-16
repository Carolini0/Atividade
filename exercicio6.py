'''
6- Crie uma classe Pessoa com características como nome, idade e altura. 
Inclua métodos para definir e obter essas informações, além de um método para cumprimentar a pessoa.
'''

# DECLARANDO A CLASSE:
class Pessoa:
    # CRIANDO FUNÇÃO NA CLASSE
    def __init__(self):
        self.nome = input('digite seu nome: ')
        self.idade = int(input('Digite sua idade: '))
        self.altura = float(input('Digite sua altura: '))

    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def informacoes(self):
        return f'Seu nome é {self.nome}, de idade {self.idade}, e altura de {self.altura}.'
    
    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def cumprimentar(self):
        return f'Olá {self.nome} seja bem vindo, prazer em conhecer você colega!'

# DECLARANDO VALORES PARA A FUNÇÃO DA CLASSE
if __name__=='__main__':
    pessoa1 = Pessoa()
    pessoa2 = Pessoa()

    # PRINTANDO E CONCECTANDO TODAS AS AÇÕES DOS VALORES
    print(pessoa1.informacoes())

    print(pessoa1.cumprimentar())

    print(pessoa2.cumprimentar())
    
    print(pessoa2.informacoes())

