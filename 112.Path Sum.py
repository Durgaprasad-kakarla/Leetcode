# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,targetSum):
            if root is None:
                if targetSum==0:
                    return True
                return False
            if root.left is None and root.right is None and  dfs(None,targetSum-root.val):
                return True
            if root.left:
                if dfs(root.left,targetSum-root.val):
                    return True
            if root.right:
                if dfs(root.right,targetSum-root.val):
                    return True
            return False
        if root is None:
            return False
        return dfs(root,targetSum)
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
