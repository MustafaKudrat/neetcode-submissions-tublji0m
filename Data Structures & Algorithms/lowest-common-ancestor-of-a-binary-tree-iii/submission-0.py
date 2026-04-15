"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pStart, qStart = p, q

        while p != q:
            p = p.parent if p.parent else qStart
            q = q.parent if q.parent else pStart
        
        return p