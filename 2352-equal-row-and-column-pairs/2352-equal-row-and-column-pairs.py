class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        row=len(grid)
        col=len(grid[0])
        columns = [[] for _ in range(col)]
        ans=0
        for c in range(col):
            for r in range(row):
                columns[c].append(grid[r][c])
            if columns[c] in grid:
                ans+=grid.count(columns[c])
        return ans