# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forests=[]
        to_delete=set(to_delete)
        def postorder(root,prev,pos): 
            if root:
                # print(root.val)
                postorder(root.left,root,'L')
                postorder(root.right,root,'R')
                if root.val in to_delete:
                    if root.left:
                        forests.append(root.left)
                    if root.right:
                        forests.append(root.right)
                    if pos=='T':
                        root.left=None
                        root.right=None
                    elif pos=='L':
                        prev.left=None
                    else:
                        prev.right=None
        postorder(root,None,'T')
        if root.left or root.right:
            forests.append(root)
        else:
            if not root.left and not root.right and root.val not in to_delete:
                forests.append(root)
        return forests
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
