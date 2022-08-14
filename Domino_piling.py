def domino_p(m,n):
    if m == 1 and n == 1:
        return 0
    else:
        return int(m * n) // 2

m, n = map(int, input().split())
print(domino_p(m,n))
