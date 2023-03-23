class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        left=0
        for i in range(len(nums)):
            right=total_sum-left-nums[i]
            if right==left:
                return i
            left+=nums[i]
        return -1
        
        
        # left=0
        # right=len(nums)-1
        # while left<=right:
        #     mid=(left+right)//2
        #     if sum(nums[:mid])==sum(nums[mid+1:]):
        #         return mid
        #     if sum(nums[:mid])>sum(nums[mid+1:]):
        #         right=mid-1
        #     else:
        #         left=mid+1
        # return -1
        