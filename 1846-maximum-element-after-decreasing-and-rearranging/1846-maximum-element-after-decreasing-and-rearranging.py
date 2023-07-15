class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n=sorted(arr)
        
        if n[0]!=1:
            n[0]=1
        for i in range(1,len(n)):
            
            if abs(n[i]-n[i-1])>1:
                n[i]=n[i-1] + 1
        return max(n)