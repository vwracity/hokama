
class HashItem: 
    def __init__(self, key, value):
        self.key = key
        self.value = value


class No: 
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor): 
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.inserirRecursivo(self.raiz, valor)

    def inserirRecursivo(self, no, valor): 
        if no.valor.key < valor.key:
            if no.direita == None:
                no.direita = No(valor)
            else: 
                self.inserirRecursivo(no.direita, valor)

        #Não há tratamento de duplicatas pois não há duplicatas nas entradas, logo serão inseridas juntos com else do lado esquerdo da lista.     
        else:
            if no.esquerda == None:
                no.esquerda = No(valor)
            else: 
                self.inserirRecursivo(no.esquerda, valor)

    def buscaBinaria(self, no, chave):
        if no is None:
            return None
        
        if no.valor.key == chave: 
            return no.valor.value
        
        elif no.valor.key < chave:
            return self.buscaBinaria(no.direita, chave)
        
        elif no.valor.key > chave:
            return self.buscaBinaria(no.esquerda, chave)
        
        return None         
    
            
             
        
    def printArvore(self):
        if self.raiz == None: 
            print("None")
        else: 
            self.printArvoreRecursivo(self.raiz)
            return
    
    def printArvoreRecursivo(self, no):
        if no == None: 
            return
        
        
    

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
        
        hi = HashItem(key, value)  #Cria o HashItem
        
        hv = self.hash(key) % self.size #Aplica função Hash na chave, hv (hashValue)
        
        if self.slots[hv] != None:    
            self.slots[hv].inserir(hi)

        else:
            self.slots[hv] = Arvore()
            self.slots[hv].inserir(hi)
            
        return
    
    #Passa o hash na chave para saber em qual slots está, se estiver não estiver nulo,
    #chama buscaBinaria na classe Arvore Binaria.
    def buscaNaTable(self, chave):
        posicaoTable = self.hash(chave) % self.size
        
        arvore = self.slots[posicaoTable]
        if arvore == None:
            return
        else: 
            return arvore.buscaBinaria(arvore.raiz, chave)
    
    def printTable(self):
        for i in self.slots: 
            print(i.printArvore)
        return
            
            

            
        
        
        
    
def Programa():
    TabelaA = parteA()
    entrada = input()
    entrada = entrada.split(" ", 1)
    
    if entrada[0] == "r":
        X = TabelaA.buscaNaTable(entrada[1])
        if X == None:
            print(f"{entrada[1]}\nNão Encontrado")
        else:
            print(f"{entrada[1]}\n{X}\n")
    
    if entrada[0] == "p" and entrada[1] == "r":
        print(TabelaA.printTable)
    
    
    

def parteA(): 
    Table = HashTable()
    #Inicializa a tabela hash A
    with open("t01/craft.txt", mode="r", encoding="utf-8") as crafts: 
            itens = []
            contador = 0
            contadorDeLinhas = False

            #Processa os dados do craft.txt
            for linha in crafts: 
                linha = linha.strip()
                if linha == "":
                    juntaLista = "\n".join(itens)
                    valor = juntaLista
                    #Adiciona dados na tabela hash A
                    Table.put(chave, valor)
                    #----------------
                    contador+=1
                    itens = []
                    contadorDeLinhas = False
                elif contadorDeLinhas == False:
                    chave = linha
                    contadorDeLinhas = True
                else: 
                    itens.append(linha)
                    contadorDeLinhas = True
        
        
        
    print("HashTable adicionada com sucesso.")
    return Table


if __name__ == "__main__":
    c = Programa()


