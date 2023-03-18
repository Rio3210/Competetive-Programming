class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        while high >= low:
            mid = low + (high - low) // 2
            if(nums[mid] == target):
                return mid
            elif(target > nums[mid]):
                low = mid+1
            else:
                high = mid - 1
        return low
        # n=len(nums)
        # for i in range(n):
        #     if nums[i]>=target:
        #         return i
        # return n