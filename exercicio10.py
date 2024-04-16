'''
10-Crie uma classe Pedido para representar um pedido feito em um restaurante. 
Inclua atributos como itens do pedido, total a ser pago e status do pedido. 
Adicione métodos para adicionar itens ao pedido, calcular o total e alterar o status.
'''
# Entendendo os itens do pedido, total a ser pago e status do pedido.

# DECLARANDO A CLASSE:
class Pedido:
    # CRIANDO FUNÇÃO NA CLASSE
    def __init__(self,item,total,status):
        self.item = item
        self.total = total
        self.status = status

    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def adicionar(self):
        return f'O seu pedido da {self.item} foi adicionado!'
    
    def valor_total(self):
        return f'O valor total a ser pago é: {self.total}'
    
    def alterar_status(self):
        return f'O seu pedido está em {self.status}' 

# DECLARANDO VALORES PARA A FUNÇÃO DA CLASSE
if __name__=='__main__':
    pedido1 = Pedido('Chuteira Nike',120,'está a caminho')
    pedido2 = Pedido('Porta Chave',20, 'saindo do fornecedor')
    pedido3 = Pedido('Geladeira Fridge',4500,'compra realizada com sucesso')

    # PRINTANDO E CONCECTANDO TODAS AS AÇÕES DOS VALORES
    print(pedido1.adicionar())
    print(pedido1.valor_total())
    print(pedido1.alterar_status())
    
    print(pedido2.adicionar())
    print(pedido2.valor_total())
    print(pedido2.alterar_status())

    print(pedido3.adicionar())
    print(pedido3.valor_total())
    print(pedido3.alterar_status())
