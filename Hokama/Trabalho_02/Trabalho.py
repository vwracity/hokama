import csv

def LerArquivo(arquivo):
    
    with open (str(arquivo), mode="r", newline="", encoding="utf-8") as file: 
        
        reader = csv.reader(file)
        next(reader)
        tabela = []

        for coluna in reader: 
            linhas = []
            linhas.append(coluna[0]) # Nome
            linhas.append(float(coluna[1])) # Fofura
            linhas.append(float(coluna[2])) # Ameaça
            linhas.append(float(coluna[3])) # Insanidade
            linhas.append(float(coluna[4])) # Tamanho
            linhas.append(float(coluna[5])) # Habilidade 
            linhas.append(float(coluna[6])) # Comédia
            tabela.append(linhas)
        
        
        #for linhas in tabela: 
        #    print(linhas)
        

        return tabela
        
  
        

def Progama(): 
    arquivo = input()
    tabela = LerArquivo(arquivo)
    numUsuarios = int(input())
    usuarios = []
    for i in range(numUsuarios):
        pesos = input()
        pesos = pesos.split(' ')
        pesos = [int(i) for i in pesos]
        print(pesos)
        usuarios.append(pesos)
    
    CalculaNota(usuarios, tabela)

def CalculaNota(usuarios, tabela):

    ListaNotas = []
    for i in range(len(tabela)):
        soma = (
                tabela[i][1] * usuarios[0][0] +  # Fofura
                tabela[i][2] * usuarios[0][1] +  # Ameaça
                tabela[i][3] * usuarios[0][2] +  # Insanidade
                tabela[i][4] * usuarios[0][3] +  # Tamanho
                tabela[i][5] * usuarios[0][4] +  # Habilidade 
                tabela[i][6] * usuarios[0][5]    # Comédia
                )
        brainrotComNota = [tabela[i][0], soma] # Nome, nota
        ListaNotas.append(brainrotComNota)

    for i in ListaNotas:
        print(i)

Progama()
#LerArquivo('brainrot.csv')