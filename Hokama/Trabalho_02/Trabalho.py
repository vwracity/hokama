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
    #print(ListaDosRankings)

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
        elif listaA[i][1] > listaB[j][1]:
            lista.append(listaB[j])
            j += 1
        else:                          # Se a pontuacao for igual dará preferência a ordem lexicografica.
            if listaA[i][0] <= listaB[j][0]:
                lista.append(listaB[j])
                j += 1
            else:  
                lista.append(listaA[i])
                i += 1

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
    # Lista[] = Ranking ordenado da lista de usuarios
    # Lista[][] = Lista da lista de [Brainrot, nota]
    # Lista[][][] = Brainrot ou nota

    # Dicionario soma tudo de forma simples com algoritmo O(1), vulgo tabela hash,
    # porem ainda sem ordenação.

    dicionario = {}
    for i in range(len(lista)):
        contador = 0
        for j in range(len(lista[0])):
            dicionario[lista[i][j][0]] = dicionario.get(lista[i][j][0], 0) + contador
            contador += 1

    # Converte tudo isso pra uma lista de tuplas para ser possivel ordenar reutilizando
    # o codigo mergeSort que foi adaptado para receber uma Lista de [brainrot, nota].
    ranking = list(dicionario.items())

    return mergesort(ranking)


def Progama():
    # Ler o input, e o csv desejado.
    arquivo = input()
    tabela = LerArquivo(arquivo)
    numUsuarios = int(input())
    usuarios = []
    for i in range(numUsuarios):
        pesos = input()
        pesos = pesos.split(' ')

        # Corrige os espaços no final da enutrada
        pesosLimpos = []
        for i in range(len(pesos)):
            if pesos[i].strip() != '':
                pesosLimpos.append(int(pesos[i].strip()))

        usuarios.append(pesosLimpos)
    # Parte A
    RankingPorUsuario = CalculaNota(usuarios, tabela)
    # Parte B
    tabelaB = CalculaTabelaB(RankingPorUsuario)

    for brainrot, pontuacao in reversed(tabelaB):
        print(f'{brainrot} {pontuacao}')


if __name__ == "__main__":
    Progama()
