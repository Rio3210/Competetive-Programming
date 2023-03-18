class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.sort()
        # low=0
        # high=len(nums)-1
        # mid=(low+high)//2
        # while low<=high:
        #     if nums[mid]==target:
        #         return mid
        #     if nums[mid]>target:
        #         low=mid+1
        #     if nums[mid]<target:
        #         high=mid-1      
        # return len(nums)
        n=len(nums)
        for i in range(n):
            if nums[i]>=target:
                return i
        return n