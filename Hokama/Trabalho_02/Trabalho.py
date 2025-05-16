import csv


def LerArquivo(arquivo):

    with open(str(arquivo), mode="r", newline="", encoding="utf-8") as file:

        reader = csv.reader(file)
        next(reader)
        tabela = []

        for coluna in reader:
            linhas = []
            linhas.append(coluna[0])  # Nome
            linhas.append(float(coluna[1]))  # Fofura
            linhas.append(float(coluna[2]))  # Ameaça
            linhas.append(float(coluna[3]))  # Insanidade
            linhas.append(float(coluna[4]))  # Tamanho
            linhas.append(float(coluna[5]))  # Habilidade
            linhas.append(float(coluna[6]))  # Comédia
            tabela.append(linhas)

        # for linhas in tabela:
        #    print(linhas)

        return tabela

# Calcula nota e depois faz MergeSort para deixa-las em ordem crescente.


def CalculaNota(usuarios, tabela):

    ListaDosRankings = []
    for j in range(len(usuarios)):
        RankingDeNotasPorUsuario = []
        for i in range(len(tabela)):
            soma = (
                tabela[i][1] * usuarios[j][0] +  # Fofura
                tabela[i][2] * usuarios[j][1] +  # Ameaça
                tabela[i][3] * usuarios[j][2] +  # Insanidade
                tabela[i][4] * usuarios[j][3] +  # Tamanho
                tabela[i][5] * usuarios[j][4] +  # Habilidade
                tabela[i][6] * usuarios[j][5]    # Comédia
            )
            brainrotComNota = [tabela[i][0], soma]  # Nome, nota
            RankingDeNotasPorUsuario.append(brainrotComNota)
        ListaDosRankings.append(RankingDeNotasPorUsuario)

    for i in range(len(ListaDosRankings)):
        ListaDosRankings[i] = mergesort(ListaDosRankings[i])

    return ListaDosRankings


# Algoritmos de sort
def merge(listaA, listaB):
    lista = []
    i = 0
    j = 0
    while i < len(listaA) and j < len(listaB):
        if listaA[i][1] < listaB[j][1]:
            lista.append(listaA[i])
            i += 1
        else:
            lista.append(listaB[j])
            j += 1

    while i < len(listaA):
        lista.append(listaA[i])
        i += 1

    while j < len(listaB):
        lista.append(listaB[j])
        j += 1
    return lista


def mergesort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    listaA = mergesort(lista[:meio])
    listaB = mergesort(lista[meio:])
    return merge(listaA, listaB)

# ---------------------------------------------------


def CalculaTabelaB(lista):
    ranking = []
    #Lista[] = Ranking ordenado da lista de usuarios
    #Lista[][] = Pequena lista do modelo [Brainrot, nota]
    #Lista[][][] = Brainrot ou nota
    for i in range(len(lista)):
        contador = 0  
        for j in range(len(lista[0])):
            if len(ranking) != len(lista[0]):
                pontos = contador
                brainrotPontuacao = [lista[i][j][0], pontos] 
                ranking.append(brainrotPontuacao)        
                contador+=1
            else: 
                ranking[j][1]+=contador
                contador+=1
    
    print(ranking)


def Progama():
    arquivo = input()
    tabela = LerArquivo(arquivo)
    numUsuarios = int(input())
    usuarios = []
    for i in range(numUsuarios):
        pesos = input()
        pesos = pesos.split(' ')
        pesos = [int(i) for i in pesos]
        usuarios.append(pesos)
    # Parte A
    RankingPorUsuario = CalculaNota(usuarios, tabela)
    # Parte B
    CalculaTabelaB(RankingPorUsuario)


Progama()
# LerArquivo('brainrot.csv')
