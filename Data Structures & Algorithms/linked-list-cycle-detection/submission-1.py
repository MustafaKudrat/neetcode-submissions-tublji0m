# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast and slow pointers
        # Floyd's Turtoise and hare

        slow, fast = head, head
        
        # slow moves 1 and fast moves 2 speed
        while slow.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            # fast catches up slow again
            if slow == fast:
                return True

        return False