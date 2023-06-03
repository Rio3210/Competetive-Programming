class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(manager, informTime, adjList):
            maxTime = 0
            for subordinate in adjList[manager]:
                maxTime = max(maxTime,dfs(subordinate, informTime, adjList))
            return maxTime + informTime[manager]

       
        adjList = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                adjList[manager[i]].append(i)

        return dfs(headID, informTime, adjList)