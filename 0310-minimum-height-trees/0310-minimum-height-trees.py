class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        adj=defaultdict(set)
        
        for i,j in edges:
            adj[j].add(i)
            adj[i].add(j)
        
        queue=deque()
        
        for i in adj:
            if len(adj[i])==1:
                queue.append(i)
        # print(queue)
        
        while n>2:
            lenn=len(queue) #num of leaves
            n=n-lenn
            
            for i in range(lenn):
                node=queue.popleft()
                for k in adj[node]:
                    adj[k].remove(node)
                    if (len(adj[k]))==1: # appending those which become leaf node
                        queue.append(k)
        return list(queue)
    