class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        i = 2
        while i*i<=n:
            if n%i == 0: 
                ans+=i
                n/=i
            else:
                i+=1
        if n!=1:
            ans+=n
        return(int(ans))