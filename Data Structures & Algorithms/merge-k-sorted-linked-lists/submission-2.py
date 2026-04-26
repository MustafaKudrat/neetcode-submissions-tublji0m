# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1:
            return None
        def mergeList(l1, l2):
            dummy = ListNode()
            res = dummy #ListNode(0, dummy)
            while l1 and l2:
                if l1.val <= l2.val:
                    dummy.next = l1 
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            
            #if l1:
            #    dummy.next = l1
            #if l2:
            #    dummy.next = l2
            dummy.next = l1 or l2
            return res.next

        
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    mergedList.append(mergeList(lists[i], lists[i + 1]))
                else:
                    mergedList.append(mergeList(lists[i], None))
            lists = mergedList

        return lists[0]