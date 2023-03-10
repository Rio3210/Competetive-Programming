class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        k = k-1 
        inx = 0
        li = [i for i in range(1,n+1)]
        def cal(k,inx):
            if len(li) == 1:
                return li[0]
            inx = (inx + k)% len(li)
            li.pop(inx)
            return cal(k,inx)
        return cal(k,inx)
