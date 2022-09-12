
class Solution(object):
    def PredictTheWinner(self, nums):
        
        def helper(nums,score_1,score_2,if_1):
            if len(nums) == 0:
                return score_1 >= score_2
            if if_1:
                res = helper(nums[1:],score_1+nums[0],score_2,not if_1) or helper(nums[:-1],score_1+nums[-1],score_2,not if_1)
                return res
            else:  
                res = helper(nums[1:],score_1,score_2+nums[0],not if_1) and helper(nums[:-1],score_1,score_2+nums[-1],not if_1)
                return res
            
        return helper(nums,0,0,True)
