class Livro:
    def __init__(self,titulo,autor,numero_pag):
        self.titulo= titulo
        self.autor = autor 
        self.numero_pag = numero_pag 

    def informacoes(self):
        print("livro:", self.titulo)
        print("Autor:", self.autor)
        print("Numero de paginas:", self.numero_pag)
    
    def calcular_palavras_por_paginas (self , total_palavras):
        return total_palavras/self.numero_pag
        

if __name__=="__main__":
    Livro = Livro ("Dom quixote", "Miguel  de Cervantes", 280)
    Livro.informacoes()


    total_palavras = 320000
    palavras_por_pagina = Livro.calcular_palavras_por_paginas(total_palavras)
    print ("Palavras por paginas:", palavras_por_pagina)
    
   
   