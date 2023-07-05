class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        left=height[0]
        right=height[-1]
        start=1
        end=len(height)-2
        while start<=end:
            
            left=max(left,height[start])
            right=max(right,height[end])
            
            if left < right:
                ans = ans + left - height[start]
                start = start + 1
            else:
                ans = ans + right - height[end]
                end = end - 1
        return ans