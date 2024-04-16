'''
4-Crie uma classe Produto que represente um item em uma loja.
 Inclua atributos como nome, preço e quantidade em estoque. 
 Adicione métodos para atualizar o estoque e calcular o preço total com base na quantidade desejada.

'''
# DECLARANDO A CLASSE:
class Produto:
    # CRIANDO FUNÇÃO NA CLASSE
    def __init__(self,nome,preco,quantidade_em_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque
        self.venda = int(input('Quantos produtos vendeu: '))
        self.armazenar = []

# Quero reduzir a quantidade vendida na quantidade de estoque
    
    def atualizar(self,produto):
        while self.venda > 0:
            self.armazenar.append(self.quantidade_em_estoque - self.venda)
            return f'Agora você tem {self.quantidade_em_estoque - self.venda} {produto} em estoque.'
      
    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def calculo(self):
        quantidade_desejada = int(input('Quantos produtos deseja: '))
        return f'O valor total é: {self.preco * quantidade_desejada} R$'
    
            
        
# DECLARANDO VALORES PARA A FUNÇÃO DA CLASSE
if __name__=='__main__':
    produto1 = Produto('Detergente', 4.50, 60)
    produto2 = Produto('Macarrão', 17, 200,)

    # PRINTANDO E CONCECTANDO TODAS AS AÇÕES DOS VALORES
    print(produto1.atualizar('Detergente'))
    print(produto2.atualizar('Macarrão'))
    print(produto1.calculo())
    print(produto2.calculo())
