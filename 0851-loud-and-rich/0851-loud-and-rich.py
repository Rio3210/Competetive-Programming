class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        length = len(quiet)
        arr = [i for i in range(length)] # to keep my answer
        indegree = [0]*length # keep those with indegrees
        graph =defaultdict(list) # to create my graph (directed graph)
        dq = deque()
        
        for i,j in richer:
            graph[i].append(j)
            indegree[j]+=1
            #increase the indegree 
        
        for i in range(length):
            if not indegree[i]:
                dq.append(i)
        # print(dq)
        
        while dq:
            n=dq.popleft()
            for v in graph[n]:
                indegree[v]-=1
                if quiet[arr[n]]<quiet[arr[v]]:
                    arr[v]=arr[n]
                if not indegree[v]:
                    dq.append(v)
                    
        return arr
        
         
        
        
        
        
        