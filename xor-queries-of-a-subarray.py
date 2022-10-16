class Solution(object):
    def xorQueries(self, arr, queries):
        
        res=[0]
        for i in arr:
            res.append(res[-1]^i)
        final_res=[]
        for query in queries:
            low,high=query
            final_res.append(res[low]^res[high+1])
        return final_res
            
            
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
