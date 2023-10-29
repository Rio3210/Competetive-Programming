class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0] * numCourses
        adj=[[] for i in range(numCourses)]
        
        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
            indegree[prerequisites[i][0]]+=1
        
        queue=deque([])
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        
        visited=0
        while queue:
            n=queue.popleft()
            visited+=1
            
            for n in adj[n]:
                indegree[n]-=1
                if indegree[n]==0:
                    queue.append(n)
        return numCourses==visited
            