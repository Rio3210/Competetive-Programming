# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
       
        def mergeSort(arr):
            if len(arr)>1:
                mid=len(arr)//2
                left_list=arr[:mid]
                right_list=arr[mid:]
                mergeSort(left_list)
                mergeSort(right_list)
                i=0
                j=0
                k=0
                while i<len(left_list) and j<len(right_list):
                    if left_list[i]<right_list[j]:
                        arr[k]=left_list[i]
                        i=i+1
                        k=k+1
                    else:
                        arr[k]=right_list[j]
                        j=j+1
                        k=k+1
                while i<len(left_list):
                    arr[k]=left_list[i]
                    i=i+1
                    k=k+1
                while j<len(right_list):
                    arr[k]=right_list[j]
                    j=j+1
                    k=k+1
        mergeSort(arr)
        print(arr)
        n=len(arr)
        ans=temp=ListNode(0)
        for i in range(n):
            temp.next=ListNode(arr[i])
            temp=temp.next
        return ans.next
            