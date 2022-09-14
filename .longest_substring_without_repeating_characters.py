class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res=""
        l,r=0,0
        h=0
        while(r!=len(s)):
            if(s[r] in res):
                l+=1
                r=l
                res=""
            res+=s[r]
            h=max(h,r-l+1)
            r+=1
        return h
        
        
        """
        :type s: str
        :rtype: int
        """
        
