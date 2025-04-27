
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
        elif no.valor.key > valor.key:
            if no.esquerda == None:
                no.esquerda = No(valor)
            else: 
                self.inserirRecursivo(no.esquerda, valor)
        
        #Se o valor for igual erá apendar na string.
        else: 
            if not isinstance(no.valor.value, list):
                aux = no.valor.value
                no.valor.value = []
                no.valor.value.append(aux)
                no.valor.value.append(valor.value)
            else:
                no.valor.value.append(valor.value)
            

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
    
            
             
    def printArvore(self, no):
        if no == None:
            return None
        else:
            return (no.valor.key, self.printArvore(no.esquerda), self.printArvore(no.direita)) 
        
    

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
            if i is None:
                print(None)
            else:
                print(i.printArvore(i.raiz))
        return
            
            

            
        
        
        
    
def Programa():
    TabelaA, TabelaB = processaTxt()
    entrada = input()
    entrada = entrada.split(" ", 1)
    
    while entrada[0] != "q": 

        if entrada[0] == "r":
            X = TabelaA.buscaNaTable(entrada[1])
            if X == None:
                print(f"{entrada[1]}\nNão Encontrado")
            else:
                print(f"{entrada[1]}\n{X}")
        
        if entrada[0] == "p" and entrada[1] == "r":
            print(TabelaA.printTable())
        
        if entrada[0] == "i":
            X = TabelaB.buscaNaTable(entrada[1])
            if X == None:
                print(f"{entrada[1]}\nNão Encontrado")
            else:
                print(f"{entrada[1]}")
                for i in X:
                    print(f"{i}")
        
        if entrada[0] == "p" and entrada[1] == "i":
            print(TabelaB.printTable())
        
        entrada = input()
        entrada = entrada.split(" ", 1)
        
    
    
    

def processaTxt(): 
    TableA = HashTable()
    TableB = HashTable()
    #Inicializa a tabela hash A
    with open("t01/craft.txt", mode="r", encoding="utf-8") as crafts: 
            itens = []
            contadorDeLinhas = False

            #Processa os dados do craft.txt
            for linha in crafts: 
                linha = linha.strip()
                if linha == "":
                    #ParteA
                    juntaLista = "\n".join(itens)
                    valorA = juntaLista
                    TableA.put(chaveA, valorA)
                    itens = []
                    contadorDeLinhas = False
                    
                elif contadorDeLinhas == False:
                    chaveA = linha
                    #Parte B
                    valorB = linha
                    
                    contadorDeLinhas = True
                else: 
                    itens.append(linha)
                    #Parte B
                    chaveB = linha.rsplit(" ", 1)
                    TableB.put(chaveB[0], valorB)
                    
                    contadorDeLinhas = True

                # racicionio para botar na tabela B  
                # linha = linha.strip()    
                # if linha in crafts:
                    
                    
                # elif contadorDeLinhas == False:
                #     valorB = linha
                #     contadorDeLinhas = True
                # else: 
                #    chaveB = linha
                #    Table.put(chaveB, valorB)
    print(TableB.slots[1])               
                    
        
        
        
    print("HashTable adicionada com sucesso.")
    return TableA, TableB


if __name__ == "__main__":
    c = Programa()


