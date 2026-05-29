# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        x = min(p.val,q.val)
        y = max(p.val,q.val)
        def dfs(node):
            if not node:
                return node
            if x <= node.val <= y:
                return node
            elif node.val > x and node.val > y:
                return dfs(node.left)
            elif node.val < x and node.val < y:
                return dfs(node.right)
        return dfs(root)