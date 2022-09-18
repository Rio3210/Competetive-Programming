class Solution(object):
    def productExceptSelf(self, nums):
        temp=1
        prod=[1]*len(nums)
        
        for i in range(len(nums)):
            prod[i] = temp
            temp = temp*nums[i]
            
        temp=1
        for i in range(len(nums)-1,-1,-1):
            prod[i] = prod[i]* temp
            temp = temp*nums[i]
            
        return prod
            
        
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
