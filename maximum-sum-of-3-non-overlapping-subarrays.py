class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        dp = [[0 for _ in range(4)] for _ in range(len(nums)+1)]
        ans = []
        sums = [0]
        for i in range(len(nums)):
            sums += [sums[-1] + nums[i]]
        
        
        for i in range(len(nums)-1,-1,-1):
            for l in range(1,4):
                take = 0
                if len(nums) - i >= k*l:
                    take = (sums[i+k]-sums[i]) + dp[i+k][l-1]
                nottake = dp[i+1][l]
                dp[i][l] = max(take,nottake)
                
        r = 0
        c = 3
        while r < len(nums) and c >= 0:
           
            if r+k <= len(nums) and sums[r+k]-sums[r] + dp[r+k][c-1] == dp[r][c]:
                ans += [r]
                r = r+k
                c -= 1
            else:
                r += 1
        return ans
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
