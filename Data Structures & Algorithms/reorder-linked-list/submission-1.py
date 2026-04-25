# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle node
        # reverse the right half
        # merge left and right half

        if not head or not head.next:
            return 

        # find mid node
        slow, fast = head, head.next ### KEY ###
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        rh = slow.next
        slow.next = None
        
        # reverse rh
        prev = None
        curr = rh
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        rh = prev

        # merge lf and rh
        lf = head
        r = rh

        while r: # check the shorter one which is r
            lTemp = lf.next
            lf.next = r
            rTemp = r.next
            r.next = lTemp
            lf = lTemp
            r = rTemp

