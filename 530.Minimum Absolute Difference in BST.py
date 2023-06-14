# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(root,list1):
            if root:
                inorder(root.left,list1)
                list1.append(root.val)
                inorder(root.right,list1)
        list1=[]
        inorder(root,list1)
        mini=float(inf)
        for i in range(1,len(list1)):
            mini=min(mini,list1[i]-list1[i-1])
        return mini
''' Time Complexity--o(n)
    Space Complexity--o(n)'''
