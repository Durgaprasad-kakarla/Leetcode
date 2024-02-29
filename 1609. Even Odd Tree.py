# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue=deque()
        queue.append(root)
        cnt=0
        while queue:
            n=len(queue)
            for i in range(n):
                node=queue.popleft()
                if cnt&1==0:
                    if node.val&1==0:
                        return False
                    else:
                        if i==0:
                            prev=node.val
                        else:
                            if prev<node.val:
                                prev=node.val
                            else:
                                return False
                else:
                    if node.val&1==1:
                        return False
                    else:
                        if i==0:
                            prev=node.val
                        else:
                            if prev>node.val:
                                prev=node.val
                            else:
                                return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            cnt+=1
        return True
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
