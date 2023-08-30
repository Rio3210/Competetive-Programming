class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        indexMap = {}
        maxLength = 0

        for i, num in enumerate(nums):
            if num in indexMap:
                indexMap[num].append(i)
            else:
                indexMap[num] = [i]
        
        for indices in indexMap.values():
            left = 0
            right = 0
            while right < len(indices):
                if (indices[right] - indices[left]) - (right - left) > k: #check this part again ?Sura
                    left += 1
                maxLength = max(maxLength, right - left + 1)
                right += 1

        return maxLength