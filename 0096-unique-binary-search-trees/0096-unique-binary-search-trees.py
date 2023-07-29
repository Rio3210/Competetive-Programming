class Solution:
    def numTrees(self, n: int) -> int:
        
        @lru_cache(None)
        def dp(n):
            if n==0 or n==1:
                return 1
            ans=0
            for i in range(1,n+1):
                ans+=dp(i-1)*dp(n-i)
            return ans
        return dp(n)