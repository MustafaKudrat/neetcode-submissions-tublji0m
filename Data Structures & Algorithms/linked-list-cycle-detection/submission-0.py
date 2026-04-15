# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Brute force using set()
        seen = set()
        curr = head

        while curr and curr.next:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next

        return False