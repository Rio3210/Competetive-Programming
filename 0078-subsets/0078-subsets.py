class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        n=len(nums)
        def helper(res,ind):
            if ind<n:
                for i in range(ind,n):
                    helper(res+[nums[i]],i+1)
            answer.append(res)
        helper([],0)
        return answer
    