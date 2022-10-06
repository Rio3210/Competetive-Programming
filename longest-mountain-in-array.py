class Solution(object):
    def longestMountain(self, A):
        high, low = [0] * len(A), [0] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]: high[i] = high[i - 1] + 1
        for i in range(len(A) - 1)[::-1]:
            if A[i] > A[i + 1]: low[i] = low[i + 1] + 1
        return max([u + d + 1 for u, d in zip(high, low) if u and d] or [0])

        """
        :type arr: List[int]
        :rtype: int
        """
        
