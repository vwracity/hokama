
class HashItem: 
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable: 
    def __init__(self):
        self.size = 29
        self.slots = [None] * self.size

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

    

class No: 
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore:
    def __init__(self):
        self.raiz = None
        self.Ordem = Fila()

    def inserir(self, valor): 
        if self.raiz == None:
            self.raiz = No(valor)
            self.Ordem.enfileirar(self.raiz)
        else:
            NoAnalisado = self.Ordem.peek()
            if NoAnalisado.esquerda == None: 
                NoAnalisado.esquerda = No(valor)
                self.Ordem.enfileirar(NoAnalisado.esquerda)

            elif NoAnalisado.direita == None:
                NoAnalisado.direita = No(valor)
                self.Ordem.enfileirar(NoAnalisado.direita)
                self.Ordem.desenfileirar()

    def imprimir_arvore(self):
        if self.raiz is None:
            print("Árvore vazia")
            return
        
        print("Estrutura da árvore:")
        self._imprimir_no(self.raiz, 0)
    
    def _imprimir_no(self, no, nivel):
        if no is None:
            return
        
        # Imprime o nó atual com indentação baseada no nível
        print("  " * nivel + f"└─ {no.valor}")
        
        # Imprime os filhos (se existirem)
        if no.esquerda is not None or no.direita is not None:
            if no.esquerda is not None:
                self._imprimir_no(no.esquerda, nivel + 1)
            else:
                print("  " * (nivel + 1) + "└─ None")
                
            if no.direita is not None:
                self._imprimir_no(no.direita, nivel + 1)
            else:
                print("  " * (nivel + 1) + "└─ None")
    
    
        

            
            
                
    
        
            

                
class Fila:
    def __init__(self):
        self.fila = []

    def enfileirar (self, item):
        self.fila.append(item)

    def desenfileirar(self):
        if not self.filaVazia():
            return self.fila.pop(0)
        
    
    def filaVazia(self): 
        return len(self.fila) == 0
    
    def tamanho(self):
        return len(self.fila)

    def peek(self): 
        return self.fila[0]
     
if __name__ == "__main__":
    A = Arvore()
    A.inserir(1)
    A.inserir(2)
    A.inserir(3)
    A.inserir(4)
    A.inserir(5)
    A.inserir(6)
    A.inserir(7)
    A.inserir(8)
    raiz = A.raiz
    A.imprimir_arvore()



