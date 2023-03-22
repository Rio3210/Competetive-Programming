class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        sl=len(s)
        pl=len(p)      
        cp=Counter(p)
        for i in range(sl-pl+1):
            cs=Counter(s[i:pl+i])
            if cs==cp:
                ans.append(i)
        return ans
    
    