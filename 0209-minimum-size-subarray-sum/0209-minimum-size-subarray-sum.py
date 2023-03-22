class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float(inf)
        left,curr_sum=0,0  
        for j in range(len(nums)):
            curr_sum+=nums[j]
            while curr_sum>=target:
                ans=min(ans,j-left+1)
                curr_sum-=nums[left]
                left+=1
        if ans==float(inf):
            return 0
        return ans