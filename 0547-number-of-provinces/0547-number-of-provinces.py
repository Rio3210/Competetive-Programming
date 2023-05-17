class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph[i+1].append(j+1)
                    
                   
        # print(graph)
        visited=set()
        def dfs(node):
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    dfs(i)
        ans=0
        for i in range(1,len(graph)+1):
            if i not in visited:
                dfs(i)
                ans+=1
        return ans
            
                