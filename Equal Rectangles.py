for _ in range(int(input())):
    n = int(input())                            
    a = list(map(int,input().split()))
    a.sort()
    add = a[0] * a[-1]  
    ans = True
    for i in range(len(a) // 2):
        if add != a[i] * a[-i - 1]:
            ans = False
            break
 
    for i in range(1, len(a), 2):
        if a[i] != a[i - 1]:
            ans = False
            break
 
    print("YES" if ans else "NO")
