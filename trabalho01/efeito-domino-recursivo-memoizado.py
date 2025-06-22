def mov_min(linha: list[int], n: int, h: int, memo: list[int]) -> int:
    if memo[n - 3] != None:
        ans = memo[n - 3]
    else:
        if n == 2:
            ans = 0 if linha[0] <= h else -1
        else:
            if linha [n-2] < h:
                resto = linha[n-2] - h
                sem_resto = mov_min(linha[:n-2], n - 1, h, memo)
                com_resto = mov_min(linha[:n-3] + [linha[n - 3] + resto], n - 1, h, memo)
                if sem_resto == -1 and com_resto == -1:
                    ans = -1
                elif sem_resto == com_resto:
                    ans = sem_resto
                else:
                    ans = 1 + com_resto
            elif linha[n-2] > h:
                resto = linha[n-2] - h
                com_resto = mov_min(linha[:n-3] + [linha[n - 3] + resto], n - 1, h, memo)
                if com_resto == -1:
                    ans = -1
                else:
                    ans = 1 + com_resto
            else:
                ans = mov_min(linha[:n-2], n - 1, h, memo)
    if ans != -1:
        memo[n-3] = ans
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