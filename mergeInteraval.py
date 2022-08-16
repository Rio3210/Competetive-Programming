class Solution(object):
    def merge(self, intervals):
        res=[]
        intervals.sort()
        for i in intervals:
            if res==[] or res[-1][1]<i[0]:
                res.append(i)
            else:
                res[-1][1]=max(res[-1][1],i[1])
        return res
