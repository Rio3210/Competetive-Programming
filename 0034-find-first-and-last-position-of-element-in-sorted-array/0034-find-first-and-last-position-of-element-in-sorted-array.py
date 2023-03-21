class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        stack=[]
        if target not in nums:
            return [-1,-1]
        for i in range(len(nums)):
            if nums[i]==target:
                stack.append(i)
                break
        for j in reversed(range(len(nums))):
            if nums[j]==target:
                stack.append(j)
                break
        return stack
        # left=0
        # right=len(nums)-1
        # ans=[-1,-1]
        # if len(nums)==0:
        #     return ans
        # if len(nums)==1 and target in nums:
        #     return [0,0]
        # while left<=right:
        #     mid=(left+right)//2
        #     if nums[mid]==target and (target!=nums[mid-1] and target!=nums[mid+1]):
        #         ans[0]=mid
        #         ans[1]=mid
        #         return ans
        #     if nums[mid]==target==nums[mid-1]:
        #         ans[0]=mid-1
        #         ans[1]=mid
        #         return ans
        #     elif nums[mid]==target==nums[mid+1]:
        #         ans[0]=mid
        #         ans[1]=mid+1
        #         return ans
        #     elif nums[mid]>target:
        #         right=mid-1
        #     else:
        #         left=mid+1
        # return ans
            