class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        def permuteHelper(path, remaining):
            if len(path) == len(nums):
                self.answer.append(path.copy())
                return
            
            for num in remaining:
                if num in path:
                    continue
                path.append(num)  
                newRemaining = remaining.copy()
                newRemaining.remove(num) 
                permuteHelper(path, newRemaining)
                path.pop()
                
        permuteHelper([], nums)
        return self.answer
