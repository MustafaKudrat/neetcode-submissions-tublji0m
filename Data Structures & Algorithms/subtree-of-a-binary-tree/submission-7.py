# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, nodep, nodeq):
        stack = [(nodep, nodeq)]
        while stack:
            p, q = stack.pop()
            if not p and not q:
                continue
            if p and q and p.val == q.val:
                stack.append([p.left, q.left])
                stack.append([p.right, q.right])
            else:
                return False
        return True