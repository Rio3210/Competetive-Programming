class Solution(object):
    def maxOperations(self, nums, k):
        nums = sorted(nums)
        count = 0
        start, end = 0, len(nums) - 1
        while (start < end):
            if (nums[start] + nums[end] > k):
                end -= 1

            elif (nums[start] + nums[end] < k):
                start += 1

            else:
                start += 1
                end -= 1
                count += 1
        return count
      
        
