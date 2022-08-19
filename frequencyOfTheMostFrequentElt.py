class Solution(object):
    def maxFrequency(self, nums, k):
        
        ans = 0
        sum = 0

        nums.sort()

        l = 0
        for rs, num in enumerate(nums):
            
            sum += num
            while sum + k < num * (rs - l + 1):
                sum -= nums[l]
                l += 1
            ans = max(ans, rs - l + 1)

        return ans
