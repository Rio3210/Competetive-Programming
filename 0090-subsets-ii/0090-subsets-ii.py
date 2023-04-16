class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        n=len(nums)
        nums.sort()
        def helper(res,ind):
            if ind<n:
                for i in range(ind,n):
                    if i>ind and nums[i]==nums[i-1]:
                        continue
                    helper(res+[nums[i]],i+1)
            answer.append(res)     
        helper([],0)
        return answer
    
    
    