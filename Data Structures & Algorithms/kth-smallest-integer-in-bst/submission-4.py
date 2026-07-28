# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pos = 0
        res = 0

        def inOrder(node):
            nonlocal pos, res
            if not node:
                return

            inOrder(node.left)
            pos += 1
            if pos == k:
                res = node.val
            
            inOrder(node.right)
        inOrder(root)
        return res
