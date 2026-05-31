# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def dfs(node,left,right):
            nonlocal ans
            if not node:
                return
            left1 = dfs(node.left, left, node.val)
            right1 = dfs(node.right, node.val, right)
            if left >= node.val:
                ans = False
            if right <= node.val:
                ans = False
            return node.val
        dfs(root, float('-inf'), float('inf'))
        return ans