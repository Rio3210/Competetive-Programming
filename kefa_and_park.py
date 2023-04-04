n, m = map(int, input().split())
cats = list(map(int, input().split()))
adj_list = {i: [] for i in range(n)}
 
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj_list[u - 1].append(v - 1)
    adj_list[v - 1].append(u - 1)
 
 
def dfs():
    ans = 0
    stk = [(0, -1, 0)]
    while stk:
        node, parent, cats_cnt = stk.pop()
        if cats[node]:
            cats_cnt += 1
        else:
            cats_cnt = 0
        if cats_cnt > m:
            continue
        if len(adj_list[node]) == 1 and node != 0:
            ans += 1
        for c in adj_list[node]:
            if c != parent:
                stk.append((c, node, cats_cnt))
    return ans
print(dfs())
