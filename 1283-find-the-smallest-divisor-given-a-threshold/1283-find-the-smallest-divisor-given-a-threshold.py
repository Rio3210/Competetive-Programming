class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        left=1
        right=max(nums)
        while left<right:
            mid=(left+right)//2
            temp=sum(math.ceil(n/mid) for n in nums)
            if temp>threshold:
                left=mid+1
            else:
                right=mid
        return left

            