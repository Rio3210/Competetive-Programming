from collections import defaultdict
n = int(input())

graph = defaultdict(list)
count = 0
myset = set()

for i in range(n):
   var = list(map(int, input().split()))
   for j in range(len(var)):
      if var[j] != 0:
         graph[i + 1].append(j + 1)
         if (j + 1, i + 1) in myset:
            continue
         myset.add((i+1, j+1))
         count += 1
print(count)
