# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue=deque()
        queue.append([root,-1])
        sm=0
        while queue:
            cnt=len(queue)
            for i in range(cnt):
                node,d=queue.popleft()
                if not node.left and not node.right and d==0:
                    sm+=node.val
                if node.left:
                    queue.append([node.left,0])
                if node.right:
                    queue.append([node.right,1])
        return sm
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
