n = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]

# Convert adjacency matrix to list representation
for i in range(n):
    edges = []
    for j in range(n):
        if adj_matrix[i][j] == 1:
            edges.append(j+1)
    print('{} {}'.format(len(edges), ' '.join(map(str, edges))))
