class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        forward=[]
        backward=[]
        n=len(nums)
        product=1
        for i in range(n):
            forward.append(product)
            product=nums[i]* product
            
        product=1
        for j in range(n-1,-1,-1):
            backward.append(product)
            product=nums[j] * product
            
        ans=[]
        backward=backward[::-1]
        for num in range(n):
            ans.append(forward[num] * backward[num])
        return ans
            
            