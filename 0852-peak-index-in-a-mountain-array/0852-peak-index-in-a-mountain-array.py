class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # return(arr.index(max(arr)))
        left=0
        right=len(arr)-1
        while left<right:
            mid=(left+right)//2
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]>arr[mid-1] and arr[mid]<arr[mid+1]:
                left=mid
            elif arr[mid]<arr[mid-1] and arr[mid]>arr[mid+1]:
                right=mid
            