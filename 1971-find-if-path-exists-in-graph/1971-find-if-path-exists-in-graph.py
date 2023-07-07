class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent=[i for i in range(n)]
        
        def find(x):
            if parent[x]==x:
                return x
            return find(parent[x])
        
        for u,v in edges:
            parent[find(u)]=find(v)
            
        return find(source)==find(destination)
    
    