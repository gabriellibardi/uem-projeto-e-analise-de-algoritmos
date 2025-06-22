def mov_min(linha: list[int], n: int, h: int) -> int:
    # print(linha)
    # print("i", i)
    # print("j", j)
    # if n < 2:
    #     ans = -1
    if n == 2:
        ans = 0 if linha[0] <= h else -1
    elif n == 3:
        if linha[0] <= h and linha[1] <= h:
            ans = 0
        elif (linha[0] + linha[1]) / 2 > h:
            ans = -1
        else:
            if linha[0] <= linha[1]:
                linha[1] = linha[1] + linha[0] - h
                linha[0] = h
            else:
                linha[0] = linha[0] + linha[1] - h
                linha[1] = h
            ans = 1
    else:
        pivo = (n - 2) // 2
        if linha[pivo] > h:
            # sobra = linha[pivo] - h
            # print('esq:', linha)
            # linha[pivo-1] += sobra
            esq = mov_min(linha[:pivo + 1], pivo + 2, h)
            # print('dir:', linha)
            # linha[pivo+1] += sobra
            dir = mov_min(linha[pivo:], n - pivo, h)
            # print('esq', esq)
            # print('dir', dir)
            if esq == -1 or dir == -1:
                ans = -1
            # if esq == -1 and dir != -1:
            #     ans = 1 + dir
            # elif esq != -1 and dir == -1:
            #     ans = 1 + esq
            # elif esq != -1 and dir != -1:
            #     ans = -1
            else:
                ans = 1 + min(esq, dir)
        else:
            print('esq:',linha)
            esq = mov_min(linha[:pivo + 1], pivo + 2, h)
            print('dir', linha)
            dir = mov_min(linha[pivo:], n - pivo, h)
            if esq == -1 or dir == -1:
                ans = -1
            else:
                ans = esq + dir
            # if esq == -1 and dir != -1:
            #     ans = dir
            # elif esq != -1 and dir == -1:
            #     ans = esq
            # elif esq != -1 and dir != -1:
            #     ans = esq + dir
            # else:
            #     ans = -1
    print('ans', ans)
    return ans

def main():
    while True:
        n, h = list(map(int, input().strip().split()))
        if n != -1:
            linha = list(map(int, input().strip().split()))
            print(mov_min(linha, n, h))
        else:
            break

main()