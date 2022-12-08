# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.leaf(root1)==self.leaf(root2)#Here we will compare the leaf nodes of both binary trees
    def leaf(self,root):
        if root is None:
            return []
        if root.left is None and root.right is None:#if both left and right child are none then add it to the list as it is a leaf node
            return [root.val]
        if root.left is not None and root.left is not None:#if both the left and right child of nodes are not None then get the leaf nodes and add it to the list
            return self.leaf(root.left)+self.leaf(root.right)
        if root.right is not None:#if the right child is not None then the right child will have the leaf node
            return self.leaf(root.right)
        if root.left is not None:#if the left child is not None then the left child will have the leaf node
            return self.leaf(root.left)
