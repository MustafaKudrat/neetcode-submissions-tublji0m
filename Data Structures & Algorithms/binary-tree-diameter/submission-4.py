# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0, 0
            
            leftHeight, leftDiameter = dfs(root.left)
            rightHeight, rightDiameter = dfs(root.right)

            height = 1 + max(leftHeight, rightHeight)
            diameter = max(leftDiameter, rightDiameter, leftHeight + rightHeight)

            return height, diameter
        
        return dfs(root)[1]

            
