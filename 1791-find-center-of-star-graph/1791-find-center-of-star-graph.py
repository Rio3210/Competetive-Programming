class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        ans=0
        for i in graph:
            if ans<len(graph[i]):
                ans=i
        return ans