# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue=deque([root])
        while queue:
            cnt=len(queue)
            tot=0
            for i in range(cnt):
                node=queue.popleft()
                tot+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return tot
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
