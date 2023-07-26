class Solution:
    def fib(self, n: int) -> int:
        memo={}
        
        def fib(n):
            if n==0:
                return 0
            if n==1:
                return 1
            if n in memo:
                return memo[n]
            
            res=fib(n-1) + fib(n-2)
            memo[n]=res
            return res
        return fib(n)