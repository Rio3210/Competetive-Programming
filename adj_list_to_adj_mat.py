n=int(input())
adj_mat=[[0 for i in range(n)] for j in range(n)]
# print(adj_mat)
for i in range(n):
    edges = list(map(int, input().split()))
    if edges[0]==0:
        continue
    for j in edges[1:]:
        adj_mat[i][j-1] = 1
for row in adj_mat:
    print(' '.join(map(str, row)))
