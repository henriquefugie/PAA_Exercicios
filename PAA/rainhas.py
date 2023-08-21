def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('[{}]'.format(' '.join('Q' if celula else ' ' for celula in linha)))
    print()

def eh_seguro(tabuleiro, linha, coluna, n):
    for i in range(coluna):
        if tabuleiro[linha][i]:
            return False
    for i, j in zip(range(linha, -1, -1), range(coluna, -1, -1)):
        if tabuleiro[i][j]:
            return False
    for i, j in zip(range(linha, n), range(coluna, -1, -1)):
        if tabuleiro[i][j]:
            return False
    return True

def resolver_n_rainhas(tabuleiro, coluna, n):
    if coluna >= n:
        imprimir_tabuleiro(tabuleiro)
        return
    for i in range(n):
        if eh_seguro(tabuleiro, i, coluna, n):
            tabuleiro[i][coluna] = 1
            print(f"Colocando rainha na linha {i + 1}, coluna {coluna + 1}")
            resolver_n_rainhas(tabuleiro, coluna + 1, n)
            tabuleiro[i][coluna] = 0
            print(f"Backtracking a partir da linha {i + 1}, coluna {coluna + 1}")

n = int(input("Digite o valor de N (tamanho do tabuleiro): "))
tabuleiro_de_xadrez = [[0] * n for _ in range(n)]
resolver_n_rainhas(tabuleiro_de_xadrez, 0, n)
