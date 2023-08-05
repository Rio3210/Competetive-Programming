class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        dp = [0] * n
        dp[0] = values[0] + 0
        ans = float('-inf')

        for j in range(1, n):
            ans = max(ans, dp[j-1] + values[j] - j)
            dp[j] = max(dp[j-1], values[j] + j)

        return ans