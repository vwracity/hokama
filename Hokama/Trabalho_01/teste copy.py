with open("t01/craft.txt", mode="r", encoding="utf-8") as crafts: 
    chave = []
    valor = []
    itens = []
    contador = 0
    contadorDeLinhas = 0

    for linha in crafts: 
        linha = linha.strip()
        if linha == "":
            juntaLista = "\n".join(itens)
            valor.append(juntaLista)
            contador+=1
            itens = []
            contadorDeLinhas = 0
        elif contadorDeLinhas == 0:
            chave.append(linha)
            contadorDeLinhas = 1
        else: 
            itens.append(linha)
            contadorDeLinhas = 1




#for i in range(len(chave)):
#   print(chave[i], valor[i])
for i in range(len(valor)):
    print(f"{chave[i]}\n{valor[i]}\n")






        
