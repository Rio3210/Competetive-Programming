t=int(input())
m=input()
ans=0
for i in range(t):
    if m[i]=="+":
        ans+=1
    elif m[i]=="-" and ans>0:
        ans-=1
print(ans)
