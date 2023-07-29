class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache
        def recur(start_x,start_y):
            if start_x >m or start_y>n:
                return 0
            if start_x==m and start_y==n:
                return 1
            right=recur(start_x+1,start_y)
            down=recur(start_x,start_y+1)
            return right+down
        return recur(1,1)