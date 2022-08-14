#I implemented merge sort to sort the colors 
#leet code problem 
class Solution(object):
    def sortColors(self, nums):
        
        if len(nums)>1:
            mid=len(nums)//2
            left_lst=nums[:mid]
            right_lst=nums[mid:]
            self.sortColors(left_lst)
            self.sortColors(right_lst)
            i=0
            j=0
            k=0
            while i<len(left_lst) and j<len(right_lst):
                if left_lst[i]<right_lst[j]:
                    nums[k]=left_lst[i]
                    i+=1
                    k+=1
                else:
                    nums[k]=right_lst[j]
                    k+=1
                    j+=1
            while i<len(left_lst):
                nums[k]=left_lst[i]
                i+=1
                k+=1
            while j<len(right_lst):
                nums[k]=right_lst[j]
                k+=1
                j+=1
        return nums
                    
      
        
