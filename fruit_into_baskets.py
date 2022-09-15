class Solution(object):
    def totalFruit(self, fruits):
        
        basket = {} 
        maxFruits = 0 
        windowStart = 0

        for windowEnd in range(len(fruits)):
            curFruit = fruits[windowEnd] 
            if curFruit not in basket:
                basket[curFruit] = 0 
            basket[curFruit] += 1 

            while len(basket) > 2:
                remove = fruits[windowStart]

                basket[remove] -= 1 
                if basket[remove] == 0:
                    del basket[remove] 
                windowStart += 1 
            maxFruits = max(maxFruits, windowEnd - windowStart + 1)
        return maxFruits
        """
        :type fruits: List[int]
        :rtype: int
        """
        
