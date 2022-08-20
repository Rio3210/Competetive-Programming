class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        final=[]
        
        for i in range(len(l)):
            
            list1 = nums[l[i]:r[i]+1]
            list1.sort()
            diff = list1[1]-list1[0]
            for i in range(1, len(list1)-1):
            	if list1[i+1] - list1[i] != diff:
            		final.append(False)
            		break
            else:
            	final.append(True)
        
        return final
