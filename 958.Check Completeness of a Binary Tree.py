# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def traversal(root):
            if not root:
                return None
            queue=deque([root])
            while queue:
                count1=len(queue)
                for i in range(count1):
                    x=queue.popleft()
                    if x.left and x.right is None:
                        if x.left.left or x.left.right:
                            return False
                    if x.left is None and x.right:
                        return False
                    if len(queue)>0:
                        if x.left and x.right is None or (x.left is None and x.right is None):
                            y=queue[0]
                            if y.left or y.right:
                                return False
                    if x.left:
                        queue.append(x.left)
                    if x.right:
                        queue.append(x.right)
            return True
        return traversal(root)
