class Solution(object):
    def kthLargestNumber(self, nums, k):
        m=list(map(int,nums))
        l=[]
        for i in m:
            l.append(i)
        j=sorted(l,reverse=True)
        return str(j[k-1])
