n, m = map(int,input().split())
 
x = m/n
steps = 0
 
while x%3 == 0:
	x=x/3
	steps += 1
 
while x%2 == 0:
	x =x/2
	steps += 1
 
if x == 1.0:
	print(steps)
else:
	print(-1)
