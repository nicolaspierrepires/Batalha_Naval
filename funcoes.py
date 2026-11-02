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
    texto += '______________________________      ______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

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

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

total_navios = 0
for tipo in frota_oponente:
    total_navios = total_navios + len(frota_oponente[tipo])

posicoes_atacadas = []

jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    posicao_nova = False
    while not posicao_nova:
        linha = int(input('Jogador, qual linha deseja atacar? '))
        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Jogador, qual linha deseja atacar? '))

        coluna = int(input('Jogador, qual coluna deseja atacar? '))
        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Jogador, qual coluna deseja atacar? '))

        if [linha, coluna] in posicoes_atacadas:
            print('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha, coluna))
        else:
            posicao_nova = True

    posicoes_atacadas.append([linha, coluna])
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
