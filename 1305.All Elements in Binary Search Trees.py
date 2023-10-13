# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def func(root,lst):
            if root:
                lst.append(root.val)
                func(root.left,lst)
                func(root.right,lst)
        lst=[]
        func(root1,lst)
        func(root2,lst)
        return sorted(lst)
''' Time Complexity--O((n1+n2)log(n1+n2))
    Space Complexity--O(n1+n2)'''
