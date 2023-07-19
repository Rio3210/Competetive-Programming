class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent=list(range(len(s)))
        
        def find(s):
            if parent[s]!=s:
                parent[s]=find(parent[s])
            return parent[s]
        
        def union(u,v):
            parent_u=find(u)
            parent_v=find(v)
            parent[parent_u]=parent_v
            
        
        for u,v in pairs:
            union(u,v)
        
        # print(parent)
        group_i=defaultdict(list)
        group_ch=defaultdict(list)
        N=len(s)
        for i in range(N):
            group=find(i)
            group_i[group].append(i)
            group_ch[group].append(s[i])
        res=['']*N
        for g in group_i.keys():
            idx=sorted(group_i[g])
            chs=sorted(group_ch[g])
            
            for j,c in zip(idx,chs):
                res[j]=c
        return ''.join(res)