# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        
        group = size // k

        dummy = ListNode()
        dummy.next = head
        prevGroup = dummy
        cur = head

        while group:
            nxt = cur
            for i in range(k):
                nxt = nxt.next

            # Reverse this group
            prev = nxt
            tail = cur          # will become the tail after reversing

            for i in range(k):
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            prevGroup.next = prev
            prevGroup = tail
            group -= 1
        return dummy.next


    

