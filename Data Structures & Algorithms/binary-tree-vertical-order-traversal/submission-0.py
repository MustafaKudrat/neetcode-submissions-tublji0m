# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root, 0)])
        minCol = maxCol = 0
        colMap = defaultdict(list)
        while q:
            node, c = q.popleft()
            colMap[c].append(node.val)
            if node.left:
                q.append((node.left, c - 1))
                minCol = min(minCol, c - 1)
            if node.right:
                q.append((node.right, c + 1))
                maxCol = max(maxCol, c + 1)

        return [colMap[c] for c in range(minCol, maxCol + 1)]
