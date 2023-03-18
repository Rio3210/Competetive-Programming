class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1: return x
        maxx = x;
        minn = 0;
        q = (minn+maxx)//2;
        while(minn < maxx):
            c = q * q;
            if c == x: 
                return q;
            elif c < x: 
                minn = q+1;
            else: 
                maxx=q;
            q=(minn+maxx)//2;
        return q - 1;