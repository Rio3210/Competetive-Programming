class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent={}
        
        def find(s):
            if s not in parent:
                parent[s]=s
            while s!=parent[s]:
                parent[s]=parent[parent[s]]
                s=parent[s]
            return s
        
        def union(u,v):
            parent_u=find(u)
            parent_v=find(v)
            
            if parent_u>parent_v:
                parent[parent_u]=parent_v
            else:
                parent[parent_v]=parent_u
            
        for u,v in zip(s1,s2):
            union(u,v)
            
        ans=''
        
        for s in baseStr:
            ans+=find(s)
        return ans