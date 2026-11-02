from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida

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
