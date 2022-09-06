#Recursion solution
class Solution(object):
    def isPowerOfThree(self, n):
        def recursion(n):
            if n==0:
                return False
            if n==1:
                return True
            elif n%3!=0 or n==0:
                return False
            
            return recursion(n/3)
        return recursion(n)
