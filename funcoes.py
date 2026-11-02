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
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)
    for tipo in frota:
        for navio in frota[tipo]:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1
    return tabuleiro
def afundados(frota, tabuleiro):
    quantidade = 0
    for tipo in frota:
        for navio in frota[tipo]:
            afundado = True
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
            if afundado:
                quantidade = quantidade + 1
    return quantidade
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicoes:
        if posicao[0] < 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 9:
            return False
        for tipo in frota:
            for navio in frota[tipo]:
                if posicao in navio:
                    return False
    return True
navios = {
    "porta-aviões": [4, 1],
    "navio-tanque": [3, 2],
    "contratorpedeiro": [2, 3],
    "submarino": [1, 4],
}

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

for nome in navios:
    tamanho = navios[nome][0]
    quantidade = navios[nome][1]
    i = 0
    while i < quantidade:
        print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(nome, tamanho))
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        if nome != "submarino":
            escolha = int(input('[1] Vertical [2] Horizontal >'))
            if escolha == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"
        else:
            orientacao = "vertical"

        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            i = i + 1
        else:
            print('Esta posição não está válida!')

print(frota)
