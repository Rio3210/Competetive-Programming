n = int(input())
a = [int(i) for i in input().strip().split(' ')]
TotalSwaps = 0
for i in range(n):
    newSwap = 0

    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            newSwap += 1
            
    TotalSwaps += newSwap       
    if newSwap == 0:
        break 
print("Array is sorted in " + str(TotalSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[len(a)-1]))
