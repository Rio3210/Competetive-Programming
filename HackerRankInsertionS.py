
def insertionSort1(n, arr):
    last_elt = arr[-1]
    for i in range(len(arr)-1, 0, -1):
        if arr[i-1] > last_elt:
            arr[i] = arr[i-1]
            print(" ".join(map(str, arr)))
        else:
            arr[i] = last_elt
            print(" ".join(map(str, arr)))
            break
    if arr[0] > last_elt:
        arr[0] = last_elt
        print(" ".join(map(str, arr)))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort1(n, arr)
