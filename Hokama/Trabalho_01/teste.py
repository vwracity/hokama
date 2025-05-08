with open("t01/craft.txt", mode="r", encoding="utf-8") as crafts: 
    itens = []
    item = []
    contador = 0
                        
    for linha in crafts: 
        linha = linha.strip()
        if linha == "":
            juntaLista = "\n".join(item)
            itens.append(juntaLista)
            contador+=1
            item = []
        else: 
            item.append(linha)






        
