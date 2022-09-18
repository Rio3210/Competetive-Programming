class Solution(object):
    def numberOfSubarrays(self, nums, k):
        
        
        s, ans = 0, 0
        prefixsum2freq = {0:1}
        for c in nums:
            if c & 1:
                s += 1
            if s - k in prefixsum2freq:
                ans += prefixsum2freq[s - k]
            prefixsum2freq[s] = prefixsum2freq.get(s,0) + 1
        return ans
    
    
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
