class Solution(object):
    def topKFrequent(self, nums, k):
        result=[]
        dict = collections.Counter(nums)
        for val, count in dict.items():
            if len(result)<k:
                heapq.heappush(result,(count,val))
            else:
                heapq.heappush(result,(count,val))
                heapq.heappop(result)
        l=[]
        for count, val in result:
                l.append(val)
        return l
