class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        pos_diagonal=set()
        neg_diagonal=set()
        board = [ ["."] * n for i in range(n) ]
        res=[]
        def helper(r):
            if r==n:
                copy=["".join(i) for i in board]
                res.append(copy)
            for c in range(n):
                if c in col or r+c in pos_diagonal or r-c in neg_diagonal:
                    continue
                col.add(c)
                pos_diagonal.add(r+c)
                neg_diagonal.add(r-c)
                board[r][c]="Q"
                helper(r+1)
                col.remove(c)
                pos_diagonal.remove(r+c)
                neg_diagonal.remove(r-c)
                board[r][c]="."
        helper(0)
        return res
                
                    