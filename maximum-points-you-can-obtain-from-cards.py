class Solution(object):
    def maxScore(self, cardPoints, k):   
        k = len(cardPoints) - k
        s = 0
        for i in range(k) :
            s += cardPoints[i]  
        m = s
        start = 0
        end = k
        while end < len(cardPoints) :
            s -= cardPoints[start]
            s += cardPoints[end]
            m = min(s, m)
            start += 1
            end += 1
        return sum(cardPoints) - m    
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
