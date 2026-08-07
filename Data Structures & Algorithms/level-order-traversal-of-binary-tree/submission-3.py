# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        
        leftList = self.levelOrder(root.left)
        rightList = self.levelOrder(root.right)
        if len(leftList) >= len(rightList):
            for i in range(len(rightList)):
                leftList[i] = (leftList[i] + rightList[i])
        else:
            for i in range(len(leftList)):
                leftList[i] = (leftList[i] + rightList[i])
            leftList.extend(rightList[len(leftList):])

        return [[root.val]] + (leftList)        
        
    