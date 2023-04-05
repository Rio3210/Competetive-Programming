class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n=len(nums)
        summ=0
        res=float(-inf)
        for i in range(n):
            summ+=nums[i]
            res=max(res,math.ceil(summ/(i+1)))
        return int(res)