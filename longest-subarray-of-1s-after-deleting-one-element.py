class Solution(object):
    def longestSubarray(self, nums):
        
        
        result,left,curr=0,0,1
        for i in range(len(nums)):
            if nums[i]==0:
                curr-=1
            if curr<0:
                if nums[left]==0:
                    curr+=1
                left+=1
            result=max(result,i-left)
        return result
        """
        :type nums: List[int]
        :rtype: int
        """
        
