class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0]-x[1])
        n=len(costs)
        total=0
        for i in range(n//2):
            total+=costs[i][0]
        for j in range(n//2,n):
            total+=costs[j][1]
        return total