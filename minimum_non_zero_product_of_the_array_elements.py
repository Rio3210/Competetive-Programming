class Solution(object):
    def minNonZeroProduct(self, p):
        if p<=1:
            return 1
        m=10**9+7
        last_value=pow(2,p)-1
        value=last_value-1
        n=value/2
        def pow_value(value_iterate,n):
            if n==0:
                return 1
            temp=pow_value(value,n/2)%m
            if n%2==0:
                return (temp**2)%m
            else:
                return ((temp**2)%m*value)%m
        result=pow_value(value,n)
        return (result*last_value)%m

        
