class Solution(object):
    def findKthBit(self, n, k):
        
        
        if k-1 == 2**(n-1)-1:
            return '0' if n==1 else '1'
        elif k-1<2**(n-1)-1:
            return self.findKthBit(n-1,k)
        else:
            return '1' if self.findKthBit(n-1,2**n-k)=='0' else '0'
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
