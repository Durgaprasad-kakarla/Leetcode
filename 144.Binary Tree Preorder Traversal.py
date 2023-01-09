# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root,res):
            if root:#if root is not null then append the value at root into res.
                res.append(root.val)
                dfs(root.left,res)#recursively call left node of the root
                dfs(root.right,res)#recursively call right node of the root
        res=[]
        dfs(root,res)
        return res
