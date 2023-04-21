class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        temp_sum=0
        summ={0:1}
        n=len(nums)
        for i in range(n):
            temp_sum=temp_sum+nums[i]
            if temp_sum-k in summ:
                count=count+summ[temp_sum-k]
            if temp_sum not in summ:
                summ[temp_sum]=1
            else:
                summ[temp_sum]=summ[temp_sum]+1
        return count