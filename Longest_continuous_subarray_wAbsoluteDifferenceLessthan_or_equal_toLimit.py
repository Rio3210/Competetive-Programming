from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums, limit):
        sorted_list = SortedList()
        l, max_length = 0, 0
        for r in range(len(nums)):
            sorted_list.add(nums[r])

            while sorted_list[-1] - sorted_list[0] > limit:
                sorted_list.remove(nums[l])
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length
