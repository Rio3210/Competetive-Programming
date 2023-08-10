class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def helper(s,l,r):
            res=0
            
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            return res
        res=0
        for i in range(len(s)): 
            res+=helper(s,i,i)
            res+=helper(s,i,i+1)
        return res