# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.res=total=0
        def dfs(root):
            if not root:
                return 0
            left,right=dfs(root.left),dfs(root.right)#find the left subtree and right subtee
            self.res=max(self.res,left*(total-left),right*(total-right))#maximum of the result,left subtree,right subtree
            return left+right+root.val
        total=dfs(root)
        dfs(root)
        return self.res%(10**9+7)
