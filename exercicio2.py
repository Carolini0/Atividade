class Animal:
    def __init__(self,nome,idade,raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def emitir_som (self):
        raise NotImplementedError("Método não implementado")

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")   
        print (f"idade:{self.idade} anos")  
        print (f"Raça:{self.raca}") 

class cachorro (Animal):
    def emitir_som (self):
        return "Au Au"  
    

class gato (Animal): 
    def emitir_som(self):
        return "Miau"       
    
if __name__=="__main__":
    cachorro = cachorro("Bob", 3 ,"Vira lata")
    gato = gato("Whiskers", 2 , "Castanho")

    cachorro.mostrar_informacoes ()
    print("Som:", cachorro.emitir_som())

    gato.mostrar_informacoes ()
    print("Som:", gato.emitir_som ())
    