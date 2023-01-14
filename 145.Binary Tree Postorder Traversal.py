# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:#####left child->right child->root-----Post Order Traversal
        def dfs(root,res):
            if root:
                dfs(root.left,res)
                dfs(root.right,res)
                res.append(root.val)
        res=[]
        dfs(root,res)
        return res
