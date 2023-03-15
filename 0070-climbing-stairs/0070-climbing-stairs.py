class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def helper(n, cache):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in cache:
                return cache[n]
            result = helper(n-1, cache) + helper(n-2, cache)
            cache[n] = result
            return result
        return helper(n, cache)