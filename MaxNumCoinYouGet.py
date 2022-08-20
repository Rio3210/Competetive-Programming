class Solution(object):
    def maxCoins(self, piles):
        n = len(piles)
        sortedP = sorted(piles)[::-1]
        sum=0
        for i in range(1, n//3*2+1,2):
            sum+=sortedP[i] 
        return sum
                
 
