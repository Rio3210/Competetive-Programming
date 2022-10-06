class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        if not tokens or tokens[0] > power:
            return 0
        up, down = 0, len(tokens) - 1
		
        maxval, curval = 0, 0
        
        while up <= down:
            if tokens[up] <= power:
                power -= tokens[up]
                curval += 1
                up += 1
            else:
                power += tokens[down]
                curval -= 1
                down -= 1
            maxval = max(maxval, curval)
        
        return maxval
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        
