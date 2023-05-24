class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        queue = deque([(0, 0, 1)]) 
        visited = set([(0, 0)])
        directions=[(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        while queue:
            x, y, dist = queue.popleft()
            if x == n-1 and y == n-1:
                return dist
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n or grid[nx][ny] == 1 or (nx, ny) in visited:
                    continue
                visited.add((nx, ny))
                queue.append((nx, ny, dist+1))

        return -1