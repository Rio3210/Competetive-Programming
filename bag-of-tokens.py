class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        if not tokens or tokens[0] > power:
            return 0
        up, down = 0, len(tokens) - 1
		
        maxScore, curScore = 0, 0
        
        while up <= down:
            if tokens[up] <= power:
                power -= tokens[up]
                curScore += 1
                up += 1
            else:
                power += tokens[down]
                curScore -= 1
                down -= 1
            maxScore = max(maxScore, curScore)
        
        return maxScore
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        
