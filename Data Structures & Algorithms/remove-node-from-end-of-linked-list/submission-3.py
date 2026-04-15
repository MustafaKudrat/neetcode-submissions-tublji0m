# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = dummy = ListNode()
        slow.next = head

        for i in range(n+1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        print(slow.next.next, fast)
        slow.next = slow.next.next

        return dummy.next