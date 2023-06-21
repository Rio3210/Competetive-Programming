class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_ed=[[] for i in range(numCourses)]
        for i,j in prerequisites:
            adj_ed[j].append(i)
        # print(adj_ed)
        
        indegree=[0]*numCourses
        
        for i in range(numCourses):
            for j in adj_ed[i]:
                indegree[j]+=1
        # print(indegree)
        queue=deque()
        for k in range(numCourses):
            if indegree[k]==0:
                queue.append(k)
                
        # print(queue)
        ans=[]
        while queue:
            t=queue.popleft()
            ans.append(t)
            for m in adj_ed[t]:
                if indegree[m]!=0:
                    indegree[m]-=1
                if indegree[m]==0:
                    queue.append(m)
        if len(ans)!=numCourses:
            return []
                    
        return ans
            
        