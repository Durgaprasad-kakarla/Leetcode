# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def build(preorder,i,bound):
            if i==len(preorder) or preorder[i]>bound:
                return None,i
            root=TreeNode(preorder[i])
            i+=1
            root.left,i=build(preorder,i,root.val)
            root.right,i=build(preorder,i,bound)
            return root,i
        i=0
        root,x= build(preorder,i,sys.maxsize)
        return root
