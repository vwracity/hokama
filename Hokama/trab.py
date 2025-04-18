
class HashItem: 
    def __init__(key, value):
        self.key = key
        self.value = value

class HashTable: 
    def __init__(self):
        self.size = 29
        self.slots = [None] * size

    def hash(self, key):
		mult = 1
		hash_value = 0
		for c in key:
			hash_value += mult * ord(c)
			mult += 1
		return hash_value
    
    def put(self, key, value):  
        
        hi = HashItem(key)  #Cria o HashItem
        
        hv = self.hash(key) % self.size #Aplica função Hash na chave, hv (hashValue)
        

        if self.slots != None:           
            #Appenda as folhas e os galhos da árvores
            return
        
        self.slots[hv] = hi 
        return

    def 

    class No: 
        def __init__(self, valor):
            self.valor = valor
            self.esquerda = None
            self.direita = None

    class Arvore:
        def __init__(self)
            self.raiz = None

        def inserir(self, valor): 
            if self.raiz == None:
                self.raiz = No(valor)
            else
              #inserirRecursivamente
                
        def inserirRecursivamente(self, noAtual, valor):
            if noAtual.esquerda == None: 
                noAtual.esquerda = No(valor)
                return
            if noAtual.direita == None:
                noAtual.direita = No(valor)
                return
            if noAtual.esquerda.esquerda 
                inserirRecursivamente(noAtual.esquerda, valor)
            

                


    
