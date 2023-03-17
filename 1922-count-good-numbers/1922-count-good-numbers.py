class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def pow(m,n):
            if(n == 0):
                return 1
        
            half = pow(m, n//2)

            if(n%2 == 0):
                return (half*half)%MOD

            return (m*half*half)%MOD   
        evn = n//2+n%2
        odd = n//2
        return pow(5, evn)*pow(4, odd)%MOD
        
        
#         MOD = 10**9 + 7
#         if n==1:
#             return 5
    
#         def count(i: int) -> int:
#             if i == n:
#                 return 1
#             if i%2==0:
#                 return (4 * count(i + 1)) % MOD
#             else:
#                 return (5 * count(i + 1)) % MOD

#         return count(0)
