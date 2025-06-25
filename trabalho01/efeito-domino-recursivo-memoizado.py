import sys
sys.setrecursionlimit(10000)

def mov_min(linha: list[int], n: int, h: int, sobra: int, memo: dict) -> int:
    print(n, sobra)
    if (n, sobra) in memo:
        return memo[(n, sobra)]
    if n == 2:
        ans = 0 if linha[0] + sobra <= h else -1
    else:
        if linha[n - 2] + sobra < h:
            resto = linha[n - 2] + sobra - h
            sem_sobra = mov_min(linha, n - 1, h, 0, memo)
            com_sobra = mov_min(linha, n - 1, h, resto, memo)
            if sem_sobra == -1 and com_sobra == -1:
                ans = -1
            elif sem_sobra == com_sobra:
                ans = sem_sobra
            else:
                ans = 1 + com_sobra
        elif linha[n - 2] + sobra > h:
            resto = linha[n - 2] + sobra - h
            com_sobra = mov_min(linha, n - 1, h, resto, memo)
            if com_sobra == -1:
                ans = -1
            else:
                ans = 1 + com_sobra
        else:
            ans = mov_min(linha, n - 1, h, 0, memo)
    memo[(n, sobra)] = ans
    return ans

def main():
    while True:
        n, h = list(map(int, input().strip().split()))
        if n != -1:
            linha = list(map(int, input().strip().split()))
            memo = {}
            print(mov_min(linha, n, h, 0, memo))
        else:
            break

main()
