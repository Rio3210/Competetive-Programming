from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    graph=defaultdict(list)
	    for i in range(len(adj)):
	        graph[i]=adj[i]
	   # {0: [1], 1: [0, 2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
	   
	    num_nodes = len(graph)
        visited = [False] * num_nodes
    
        for start_node in range(num_nodes):
            if visited[start_node]:
                continue
    
            stack = [(start_node, -1)]  # Stack to store nodes and their parent
            visited[start_node] = True
    
            while stack:
                node, parent = stack.pop()
    
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        stack.append((neighbor, node))
                        visited[neighbor] = True
                    elif parent != neighbor:
                        return 1
    
        return 0
    		#Code here


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends