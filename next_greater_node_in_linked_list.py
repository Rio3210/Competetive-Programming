# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        ans = []
        stack = []
        i = 0
        curr = head
        while(curr):
            ans.append(0)
            curr = curr.next
        while(head):
            while(stack and stack[-1][1] < head.val):
                index, _ = stack.pop()
                ans[index] = head.val
            stack.append([i, head.val])
            i += 1
            head = head.next
        return ans
        """
        :type head: ListNode
        :rtype: List[int]
        """
        
