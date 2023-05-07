class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n==1 or n==0 :
            return 0
        
        def prime(n: int):
            
            
            is_prime= [True for _ in range(n)]
            is_prime[0] = is_prime[1] = False

            i = 2

            while i * i <n:
                
                if is_prime[i]:
                    j = i * i
                    while j < n:
                        is_prime[j] = False
                        j += i
                i += 1
            return is_prime
        # print(prime(n))
        return prime(n).count(True)
