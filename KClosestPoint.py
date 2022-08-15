class Solution(object):
    def kClosest(self, arr, k):
        arr.sort(key=lambda k:k[0]**2+k[1]**2)
        return arr[:k]
