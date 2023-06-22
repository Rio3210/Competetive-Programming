class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:   
        indegree=[0]*n
        graph=defaultdict(list)
        
        dq=deque()
        for a,b in edges:
            graph[a].append(b)
            indegree[b]+=1
        # print(graph)
        
        ans=[set() for i in range(n)]
        for i in range(n):
            if not indegree[i]:
                dq.append(i)
        
        while dq:
            
            node=dq.popleft()
            
            for vertex in graph[node]:
                ans[vertex].add(node)
                ans[vertex].update(ans[node])
                indegree[vertex]-=1
                if not indegree[vertex]:
                    dq.append(vertex)
        return map(sorted,ans)
        
            
            
            