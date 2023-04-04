n,k=map(int,input().split())
arr=[]
for _ in range(n):
    f,t=map(int,input().split())
    if t>k:
        arr.append(f-(t-k))
    else:
        arr.append(f)
print(max(arr))
