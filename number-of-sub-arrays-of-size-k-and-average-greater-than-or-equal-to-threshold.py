class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        
        winsum=0
        start=0
        count=0
        for i in range(len(arr)):
            winsum+=arr[i]
            if i>=k-1:
                if (winsum/k)>=threshold:
                    count+=1
                winsum-=arr[start]
                start+=1
        return count
                
        
        
        
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        
