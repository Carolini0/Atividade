'''3-Crie uma classe chamada Conta Bancária com atributos como número da conta, saldo e titular. 
Implemente métodos para depositar dinheiro, sacar dinheiro e mostrar o saldo atual.
'''

# DECLARANDO CLASSE
class Conta_Bancaria:
    # CRIANDO FUNÇÃO NA CLASSE
    def __init__(self,numero_conta,saldo,titular):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.titular = titular

    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def depositar(self, mensagem_depositar):
        return f'A pessoa do numero da conta {self.numero_conta} esta {mensagem_depositar} .'

    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def sacar(self):
        return f'A pessoa esta sacando um valor de 800 R$ '
    
    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def saldo_atual(self):
        return f'O valor do saldo atual da conta do sujeito está em: {self.saldo - 800}.'

# DECLARANDO VALORES PARA A FUNÇÃO DA CLASSE
if __name__=='__main__':
    conta1 = Conta_Bancaria(7823, 1200, 12345678)

    # PRINTANDO E CONCECTANDO TODAS AS AÇÕES DOS VALORES
    print(conta1.depositar('depositando'))
    print(conta1.sacar())
    print(conta1.saldo_atual())
