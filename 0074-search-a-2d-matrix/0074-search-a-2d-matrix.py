class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        def binaryserach(nums):
            low=0
            high=len(nums)-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    return mid
                if nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return -1
        row=len(matrix)
        ans=-1
        for i in range(row):
            print(i)
            if matrix[i][-1]==target:
                return True
            elif matrix[i][-1]>target:
                ans=binaryserach(matrix[i])
                break

        if ans!=-1:
            return True
        else:
            return False
                