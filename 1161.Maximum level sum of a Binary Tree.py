# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue=[]
        queue.append(root)
        l=0
        level=l
        maxsum=sys.maxsize*-1
        while queue:
            count=len(queue)
            sum=0
            for i in range(count):
                node=queue.pop(0)
                sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            l+=1
            if maxsum<sum:
                maxsum=sum
                level=l
        return level
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
