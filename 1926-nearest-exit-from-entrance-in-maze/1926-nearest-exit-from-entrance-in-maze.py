class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited=set()
        row=len(maze)
        col=len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        visited.add((entrance[0],entrance[1]))
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            x,y,d=queue.popleft()
            
            for dx, dy in directions:
                dx=dx+x
                dy=dy+y
                if 0<=dx<row and 0<=dy<col:
                    if  maze[dx][dy] == "." and (dx, dy) not in  visited:
                        visited.add((dx,dy))
                        queue.append((dx,dy,d+1))
                elif (x, y) != (entrance[0], entrance[1]):
                    return d                
        return -1
            
            
            