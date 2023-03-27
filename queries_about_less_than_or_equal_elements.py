from bisect import bisect_right
 
n, m = map(int, input().split())
 
a = list(map(int, input().split()))
 
b = list(map(int, input().split()))
 
a.sort()
 
for i in range(m):
    count = bisect_right(a, b[i])
    print(count, end=' ')
