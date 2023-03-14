class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:   
        def max_p1(i,j):
            if i == j: 
                return nums[i]
            return max(nums[i] + max_p2(i+1,j), nums[j] + max_p2(i,j-1))
        
        def max_p2(i,j):
            if i == j:
                return 0        
            return min(max_p1(i+1,j), max_p1(i,j-1))
    
        return max_p1(0, len(nums)-1) >= max_p2(0, len(nums)-1)
       
        