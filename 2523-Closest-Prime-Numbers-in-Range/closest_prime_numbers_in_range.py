class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve_of_eratosthenes(n):
            primes = [True] * (n+1)
            primes[0] = primes[1] = False

            for i in range(2, int(n**0.5)+1):
                if primes[i]:
                    for j in range(i*i, n+1, i):
                        primes[j] = False

            return primes

        primes_arr = sieve_of_eratosthenes(right)
        primes = [i for i in range(left, right+1) if primes_arr[i]]

        min_diff = float('inf')
        closest_primes = [-1,-1]
        for i in range(len(primes)-1):
            diff = primes[i+1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                closest_primes = (primes[i], primes[i+1])
        return closest_primes
            
