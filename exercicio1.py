'''
1-Crie uma classe chamada Carro com atributos como marca, modelo, ano e cor. 
Adicione métodos para ligar o carro, desligar o carro e acelerar.
'''
# DECLARANDO A CLASSE:
class Carro: 
    # CRIANDO FUNÇÃO NA CLASSE
    def __init__(self,marca,modelo,ano,cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def ligar(self):
        return f'O motorista está ligando o seu carro {self.modelo}'
    
    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def desligar(self, mensagem_para_desligar):
        return f'O motorista esta {mensagem_para_desligar} seu carro.'

    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def acelerar(self, mensagem_para_acelerar):
        return f'O motorista está {mensagem_para_acelerar} seu carro {self.modelo} {self.cor}'
    
# DECLARANDO VALORES PARA A FUNÇÃO DA CLASSE
if __name__=='__main__':
    carro1 = Carro('Fiat','Cronos',2024,'Preto')
    carro2 = Carro('Chevrolet','S10',2017,'Cinza')
    carro3 = Carro('Hyundai','Creta',2020,'Vermelho')

    # PRINTANDO E CONCECTANDO TODAS AS AÇÕES DOS VALORES
    print(carro1.ligar())
    print(carro2.desligar('desligando'))
    print(carro3.acelerar('acelerando'))
