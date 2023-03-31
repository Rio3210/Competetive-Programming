class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            nonlocal visited, curr_count, ans, prev_count
            visited[node] = True
            for i in graph[node]: 
                if not visited[i]:
                    ans += prev_count
                    curr_count += 1
                    dfs(i)
        
        visited = [False] * n
        prev_count, curr_count = 0, 0
        ans = 0
        for i in range(n):
            if not visited[i]:
                prev_count = curr_count
                curr_count += 1
                ans += prev_count
                dfs(i)
        
        return ans