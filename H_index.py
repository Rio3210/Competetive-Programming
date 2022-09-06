class Solution(object):
    def hIndex(self, citations):
        m=sorted(citations,reverse=False)
        n = len(m)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if m[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1
        return n - left
