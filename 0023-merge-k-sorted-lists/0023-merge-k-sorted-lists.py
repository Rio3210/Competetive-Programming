# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        dummy = cur = ListNode()
        nodes = []
        heapify(nodes)
        for i in lists:
            while i:
                heapq.heappush(nodes,i.val)
                i = i.next
        for i in range(len(nodes)):
            cur.next = ListNode(heappop(nodes))
            cur = cur.next
        return dummy.next