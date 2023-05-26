class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [False] * len(rooms)
        visited[0] = True
        queue = deque([0])
        while queue:
            curr = queue.popleft()
            for key in rooms[curr]:
                if not visited[key]:
                    visited[key] = True
                    queue.append(key)
        # print(visited)
        return all(visited)
            