class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        a=len(s)//2
        b=len(s)-1
        for i in range(a):
            s[i],s[b]=s[b],s[i]
            b-=1
        """
        Do not return anything, modify s in-place instead.
        """
        