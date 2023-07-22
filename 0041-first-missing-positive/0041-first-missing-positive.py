class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numms=set(nums)
        
        for i in range(1,len(numms)+1):
            if i not in numms:
                return i
        return len(numms)+1