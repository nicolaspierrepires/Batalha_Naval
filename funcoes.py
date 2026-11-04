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

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto