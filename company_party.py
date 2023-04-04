n=int(input())
p=[int(input()) for i in range(n)]
# p=[-1,1,2,1,-1]
g=0
# ans=[]
for i in range(1,n+1):
	c=0
	while i>0:
		i=p[i-1]
		c+=1
# 	ans.append(c)
	g=max(g,c)
print(g)
