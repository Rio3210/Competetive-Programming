class Solution(object):
    def findAnagrams(self, s, p):
        s_dict = collections.Counter(s[:len(p)-1]) 
        p_dict = collections.Counter(p)
        start = 0
        res = []
        for i in range(len(p)-1, len(s)):
            s_dict[s[i]] += 1
            if s_dict == p_dict:
                res.append(start)
            s_dict[s[start]] -= 1
            if s_dict[s[start]] == 0:
                del s_dict[s[start]]
            start += 1
            
        return res
    
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
