# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[1]
        
    def dfs(self, root):
        if root is None:
            return (0, True)
        
        leftHeight = self.dfs(root.left)
        rightHeight = self.dfs(root.right)
        res = [0, False]

        res[1] = leftHeight[1] and rightHeight[1] and (abs(leftHeight[0] - rightHeight[0]) <= 1)
        res[0] = 1 + max(leftHeight[0], rightHeight[0])
        return res
