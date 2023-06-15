# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue=[]
        queue.append(root)
        levelsum=[]
        while queue:
            sum=0
            count=len(queue)
            for i in range(count):
                node=queue.pop(0)
                sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levelsum.append(sum)
        if len(levelsum)<k:
            return -1
        return (heapq.nlargest(k,levelsum))[-1]
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
