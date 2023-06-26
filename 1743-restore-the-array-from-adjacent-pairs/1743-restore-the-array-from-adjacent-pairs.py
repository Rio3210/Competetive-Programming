class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        adj=defaultdict(set)
        for i,j in adjacentPairs:
            adj[j].add(i)
            adj[i].add(j)
        
        queue=deque()
        # print(adj)
        
        for i in adj:
            if len(adj[i])==1:
                queue.append(i)
        # print(queue)
        ans=[]
        while queue:

            node=queue.popleft()
            ans.append(node)
            for k in adj[node]:
                adj[k].remove(node)
                if (len(adj[k]))==1:
                    queue.insert(0,k)
        return ans