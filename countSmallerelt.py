#leetCode Problem
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        list1=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count+=1
            list1.append(count)
        return list1
