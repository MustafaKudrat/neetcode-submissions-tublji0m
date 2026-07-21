# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
            
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        rightHalf = slow.next
        slow.next = None

        prev, cur = None, rightHalf
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        # prev is right most node now

        l, r = head, prev
        while r:
            ln = l.next
            l.next = r
            l = ln
            rn = r.next
            r.next = ln
            r = rn
            


