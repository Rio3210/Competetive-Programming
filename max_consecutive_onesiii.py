class Solution(object):
    def longestOnes(self, nums, k):
        maxLength = 0
        i,j = 0,0
        n = len(nums)
        zero = 0
        while(j < n):
            if(nums[j] == 0): zero += 1
            if(zero > k):
                while(zero > k):
                    if(nums[i] == 0): zero -= 1
                    i += 1
            maxLength = max(maxLength, j - i + 1)
            j += 1

        return maxLength
        
