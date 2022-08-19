class Solution(object):
    def numIdenticalPairs(self, nums):
        count=0
        k=1
        for i in (nums):
            for j in (nums[k:]):
                if i==j:
                    count+=1
            k+=1
        return count
            
        
