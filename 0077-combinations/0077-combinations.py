class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def helper(st,comb):
            if len(comb)==k:
                ans.append(comb.copy())
            for i in range(st,n+1):
                comb.append(i)
                helper(i+1,comb)
                comb.pop()
        helper(1,[])
        return ans