# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow = head.next, head

        # find mid point, slow -> one node, fast -> two nodes
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # should have slow at mid node

        # reverse the second half
        second = slow.next
        prev = slow.next = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first, second = head, prev

        # merge
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


