class Solution(object):
    def rearrangeArray(self, nums):
        nums.sort()
        mid = (len(nums)-1)//2
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
        return nums
