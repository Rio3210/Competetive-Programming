class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp=defaultdict(int)
        maxx=float('-inf')
        
        for i in arr:
            dp[i]=dp[i-difference]+1
            maxx=max(maxx,dp[i])
        return maxx