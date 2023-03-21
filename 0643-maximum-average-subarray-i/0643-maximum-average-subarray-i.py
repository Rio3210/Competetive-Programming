class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = float(-inf)
        window_sum, start = 0,0
        for i in range(len(nums)):
            window_sum += nums[i]
            if i >=k-1:
                result=max(window_sum/k,result)
                window_sum -= nums[start]
                start += 1
        return result