t=int(input())
for _ in range(t):
    
    a,b=map(int,input().split())
    print(min(min(a,b),int((a+b)/4)))
