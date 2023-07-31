class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for j in coins:
                if i-j>=0:
                    dp[i]=min(dp[i],dp[i-j]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1
        
        
#         #error not works
#         res=float('inf')
#         memo={}
#         def dp(n):
#             nonlocal res
#             if n==0:
#                 return 0
#             if n<0:
#                 return float('inf')
#             if n in memo:
#                 return memo[n]
            
#             for i in coins:
#                 res=min(res,dp(n-i)+1)
#             memo[n]=res
#             return res
#         dp(amount)
#         if res==float('inf'):
#             return -1
#         else:
#             return res
            