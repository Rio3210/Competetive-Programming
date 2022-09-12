n, l, r= [int(item) for item in input().split()]

def enum(n):
    if n <= 1:
        return 1
    else:
        return enum(n//2)*2 + 1

def _list(n):
    if n<=1:
        return n
    else:
        return 2 * _list(n//2) + n%2

def solve(p, n, temp, prev):
    if p == 0:
        return 0
    elif p == temp:
        return _list(n)
    elif p==temp//2 + 1:
        return _list(n//2) + n%2
    elif p>temp:
        return _list(n) + prev%2 + solve(p - temp - 1, n//2, temp//2, n)
    else:
        return solve(p, n//2, temp//2, n)

def help_sam(l, r, n):
    lower = solve(l - 1, n, enum(n), 0)
    higher = solve(r, n, enum(n), 0)

    return higher - lower

output  = help_sam(l, r, n)

print(output)
