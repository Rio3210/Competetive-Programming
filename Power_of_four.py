#recursion solution 
class Solution(object):
    def isPowerOfFour(self, n):
        def recursion(n):
            if n==1:
                return True
            elif n%4!=0 or n==0:
                return False
            
            return recursion(n/4)
        return recursion(n)
        
