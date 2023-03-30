
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        par, vis, deg = [0] * (n+1), [0] * (n+1), [0] * (n+1)
        temp=input().split()
        # print(temp)
        for i in range(1, n+1):
            par[i] = int(temp[i-1])
            deg[i] += 1
            deg[par[i]] += 1
        leaf = []
        for i in range(1, n+1):
            if deg[i] == 1:
                leaf.append(i)
        if n == 1:
            print("1")
            print("1")
            print("1")
            continue
        print(len(leaf))
        
        for i in leaf:
            path = []
            j = i
            while not vis[j]:
                path.append(j)
                vis[j] = 1
                j = par[j]
            print(len(path))
            path.reverse()
            print(" ".join(str(x) for x in path))

solve()

