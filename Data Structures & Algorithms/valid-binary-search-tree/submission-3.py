# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        q = deque([(root, float("-inf"), float("inf"))])
        while q:
            node, leftVal, rightVal = q.popleft()
            if not (leftVal < node.val < rightVal):
                return False
            if node.left:
                q.append((node.left, leftVal, node.val))
            if node.right:
                q.append((node.right, node.val, rightVal))
        return True