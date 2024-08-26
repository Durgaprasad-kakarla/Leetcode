"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        lst=[]
        def postorder(root):
            if root:
                for i in root.children:
                    postorder(i)
                lst.append(root.val)
        postorder(root)
        return lst
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
