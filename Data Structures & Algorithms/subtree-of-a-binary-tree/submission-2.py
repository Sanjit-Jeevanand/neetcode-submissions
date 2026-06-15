# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s1 = ""
        s2 = ""
        def dfs(node):
            nonlocal s1
            if not node:
                s1 += f"#{-101}"
                return False
            s1 += f"#{node.val}"
            dfs(node.left)
            dfs(node.right)
        def dfs2(node):
            nonlocal s2
            if not node: 
                s2 += f"#{-101}"
                return False
            s2+= f"#{node.val}"
            dfs2(node.left)
            dfs2(node.right)
        dfs(root)
        dfs2(subRoot)
        return s2 in s1