# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:    
        def BT(preorder, inorder, st, end, preindex, inindex):
            if st > end:
                return None
            root = TreeNode(preorder[preindex])
            for i in range(st, end + 1):
                if inorder[i] == root.val:
                    inindex = i
                    break
            root.left = BT(preorder, inorder, st, inindex - 1, preindex + 1, inindex)
            root.right = BT(preorder, inorder, inindex + 1, end, preindex + inindex - st + 1, inindex)
            return root
        return BT(preorder, inorder, 0, len(preorder) - 1, 0, 0)
        
