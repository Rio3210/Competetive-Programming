class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            mid_number = nums[mid]
        
            if mid_number == target:
                return mid

            if nums[lo] <= mid_number:
                # Left half is sorted
                if nums[lo] <= target and target < mid_number:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # Right half is sorted
                if mid_number < target and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1