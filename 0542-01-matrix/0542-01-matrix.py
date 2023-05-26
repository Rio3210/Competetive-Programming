class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def is_bound(row,col):
            return 0<=row<len(mat) and 0<=col<len(mat[0])
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        col=len(mat[0])
        row=len(mat)
        ans=[[-1]* col for i in range(row)]
        # print(ans)
        queue=deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    queue.append((i, j))
        # print(queue)
        while queue:
            row,col=queue.popleft()
            for dr,dc in direction:
                nr,nc=row+dr,col+dc
                if is_bound(nr,nc) and ans[nr][nc]==-1:
                    ans[nr][nc]=ans[row][col]+1
                    queue.append((nr,nc))
        return ans