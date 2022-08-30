class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        maps = {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                maps[stack.pop()] = num
            stack.append(num)
                
        return [maps.get(val,-1) for val in nums1]
