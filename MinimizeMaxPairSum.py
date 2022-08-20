class Solution(object):
    def minPairSum(self, nums):
        n=sorted(nums)
        i=0
        j=len(n)-1
        max_val=[]
        while i<j:
            max_val.append(n[i]+n[j])
            i+=1
            j-=1
        return max(max_val)
        
