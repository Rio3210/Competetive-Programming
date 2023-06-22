class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        out_degree = [0] * n
        in_degree = [[] for i in range(n)]
        for i in range(n):
            for j in graph[i]:
                out_degree[i] += 1
                in_degree[j].append(i)
        queue = deque()
        for i in range(n):
            if out_degree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            for neighbor in in_degree[node]:
                out_degree[neighbor] -= 1
                if out_degree[neighbor] == 0:
                    queue.append(neighbor)
        safe_nodes = []
        for i in range(n):
            if out_degree[i] == 0:
                safe_nodes.append(i)
        return safe_nodes
                    
        