
class Solution(object):
    def minSubArrayLen(self, target, nums):
        
        
        l,r=0,float('inf')
        curr=0
        
        for j in range(len(nums)):
            curr+=nums[j]
            while curr>=target:
                r=min(r,j-l+1)
                curr-=nums[l]
                l+=1
        if r==float('inf'):
            return 0
        else:
            return r
                
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
