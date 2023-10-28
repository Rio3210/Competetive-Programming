import heapq
from collections import defaultdict

n, m = map(int, input().split())
dic = defaultdict(list)

for _ in range(m):
    i, j, w = map(int, input().split())
    dic[i].append((w, j))
    dic[j].append((w, i))

distance = [float('inf')] *(n+1)
distance[1] = 0
min_heap = [(0, 1)]
previous = [None] * (n+1)

while min_heap:
    w, v = heapq.heappop(min_heap)

    if w > distance[v]:
        continue

    for y, k in dic[v]:
        temp = distance[v] + y
        if temp < distance[k]:
            distance[k] = temp
            previous[k] = v  
            heapq.heappush(min_heap, (temp, k))

if distance[n]==float('inf'):
    print(-1)
    exit()
path = []
node = n
while node is not None:
    path.append(node)
    node = previous[node]
path.reverse()
for node in path:
    print(node, end=' ')
