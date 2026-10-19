def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    i=0
    while i<tamanho:
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        elif orientacao == "horizontal":
            posicoes.append([linha, coluna + i])  
        i=i+1        
    return posicoes
def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):

    novasposicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if nome in frota:
        frota[nome].append(novasposicoes)
    else:
        frota[nome] = [novasposicoes]
    return frota