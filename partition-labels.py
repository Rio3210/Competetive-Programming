class Solution(object):
    def partitionLabels(self, s):
        
        dic = {c:i for i, c in enumerate(s)}
        left = 0
        right = 0
        ans = []
        for i, c in enumerate(s):
            right = max(right, dic[c])
            if i == right:
                ans += [right - left + 1]
                left = right + 1
        return ans
    
        """
        :type s: str
        :rtype: List[int]
        """
        
