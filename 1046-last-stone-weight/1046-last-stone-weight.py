class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        mxheap=[-stone for stone in stones]
        heapq.heapify(mxheap)
        while len(mxheap)>1:
            stone1=-heapq.heappop(mxheap)
            stone2=-heapq.heappop(mxheap)
            
            if stone1!=stone2:
                heapq.heappush(mxheap,-(stone1-stone2))
        if mxheap:
            return -mxheap[0]
        return 0
                