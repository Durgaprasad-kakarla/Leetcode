# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def BT(postorder, poststart,postend,inorder,instart,inend,dict1):
            if poststart>postend or instart>inend:
                return None
            root = TreeNode(postorder[postend])
            inroot=dict1[root.val]
            numsleft=inroot-instart
            root.left = BT(postorder,poststart,poststart+numsleft-1,inorder,instart,inroot-1,dict1)
            root.right = BT(postorder,poststart+numsleft,postend-1,inorder,inroot+1,inend,dict1)
            return root
        dict1={}
        for i in range(len(inorder)):
            dict1[inorder[i]]=i
        return BT(postorder, 0,len(postorder)-1,inorder,0,len(inorder)-1,dict1)
        
