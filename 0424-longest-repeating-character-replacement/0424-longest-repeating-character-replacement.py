class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        maxf=0
        res=0
        for i in range(len(s)):
            count[s[i]]=1+count.get(s[i],0)
            maxf=max(maxf,count[s[i]])
            while (i-left+1)-maxf>k:
                count[s[left]]-=1
                left+=1
            res=max(res,i-left+1)
        return res