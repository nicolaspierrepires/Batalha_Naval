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

print(frota)
