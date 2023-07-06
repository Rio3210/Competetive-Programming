class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent=[i for i in range(len(edges)+1)]
        
        def find(x):
            if parent[x]==x:
                return x 
            return find(parent[x])
        
        ans = []
        for u, v in edges:
            parent_u = find(u)
            parent_v = find(v)
            if parent_u == parent_v:
                ans = [u, v]
            else:
                parent[parent_u] = parent_v
        return ans