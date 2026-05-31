# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node,maxi):
            nonlocal ans
            if not node:
                return
            maxi = max(maxi,node.val)
            left = dfs(node.left, maxi)
            right = dfs(node.right, maxi)
            if node.val >= maxi:
                ans += 1
            return
        dfs(root, root.val)
        return ans
            