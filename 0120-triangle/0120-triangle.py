class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle)
        dp = [[0] * (i + 1) for i in range(n)]

        # Initialize the last row of dp
        dp[n-1] = triangle[n-1]

        # Iterate from the second-to-last row to the top
        for i in range(n-2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])

        return dp[0][0]
            
            
       
            