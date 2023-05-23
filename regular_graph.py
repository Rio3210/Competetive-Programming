from collections import defaultdict

def is_regular(edges):
    degree = defaultdict(int)
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1

    return len(set(degree.values())) == 1

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
if is_regular(edges):
    print("YES")
else:
    print("NO")
