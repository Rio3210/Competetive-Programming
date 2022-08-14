class Solution(object):
    def targetIndices(self, nums, target):
        for i in range(len(nums)):    # if you use bubble sort (not best algorithm)
            for j in range(len(nums)-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        l=[]
        for m in range(len(nums)):
            if nums[m]==target:
                l.append(m)
        return l
 
#solution2
class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()  #if you used built in function sort()... better than bubble sort
        l=[]
        for m in range(len(nums)):
            if nums[m]==target:
                l.append(m)
        return l
