class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        if k <= 0 or len(nums) <= 1:
            return ((nums))

        nums.reverse()
        start = k
        end = len(nums)-1
        start1 = 0
        end1= k-1

        while(start<end):
            nums[start] , nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        while(start1<end1):
            nums[start1] , nums[end1] = nums[end1], nums[start1]
            start1+=1
            end1-=1    

        return (nums)
        
        
