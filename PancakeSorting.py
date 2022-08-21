class Solution(object):
    def pancakeSort(self, arr):
        
        def reverse(l, begin, end):
            for i in range((end-begin) // 2):
                l[begin+i], l[end-1-i] = l[end-1-i], l[begin+i]

        result = []
        for n in range(len(arr),1 ,-1):
            i = arr.index(n)
            reverse(arr, 0, i+1)
            result.append(i+1)
            reverse(arr, 0, n)
            result.append(n)
        return result
