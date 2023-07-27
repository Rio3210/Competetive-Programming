class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo={}
        # n=len(nums)
        # def helper(i):
        #     if i==n-1:
        #         return nums[n-1]
        #     if i==n-2:
        #         return max(nums[n-1],nums[n-2])
        #     if i in memo:
        #         return memo[i]
        #     result=max(helper(i+1),helper(i+2) + nums[i])
        #     memo[i]=result
        #     return result
        # return helper(0)
        summ1,summ2=0,0
        for i in nums:
            temp=max(summ1+i,summ2)
            summ1=summ2
            summ2=temp
        return summ2