class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [0] * len(rooms)
        def _canVisitAllRooms(i):
            if visited[i]:
                return
            visited[i] = True
            for j in range(len(rooms[i])):
                _canVisitAllRooms(rooms[i][j])
            return
        _canVisitAllRooms(0)
        return all(visited)