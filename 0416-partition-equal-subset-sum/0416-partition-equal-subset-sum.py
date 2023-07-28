class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        memo={}
        def helper(i,half_sum):
            
            if i>=n or half_sum==0:
                return half_sum==0
            if half_sum<0:
                return False
            state = (i, half_sum)
            if state in memo:
                return memo[state]
            subtract=helper(i+1,half_sum-nums[i])
            if subtract == True:
                memo[state] = True
                return True
            
            no_subtract =helper(i+1,half_sum)
            result = subtract or no_subtract 
            memo[state] = result
            return subtract or no_subtract
        total_sum=sum(nums)
        if total_sum % 2 !=0:
            return False
        half_sum=total_sum//2
        return helper(0,half_sum)
        
	     
	     
            
