class Solution(object):
    def nextPermutation(self, nums):
        
        
        i = len(nums)-2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums)-1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        i += 1
        j = len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
