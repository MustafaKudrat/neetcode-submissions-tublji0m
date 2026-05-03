# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {val:i for i, val in enumerate(inorder)}

        self.rootIdx = 0
        def dfs(l, r):
            if l > r:
                return None
            rootVal = preorder[self.rootIdx]
            self.rootIdx += 1
            root = TreeNode(rootVal)
            mid = idx[rootVal]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root


        return dfs(0, len(inorder) - 1)