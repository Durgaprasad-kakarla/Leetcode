# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            newnode=TreeNode(val)
            newnode.left=root
            return newnode
        queue=deque()
        queue.append(root)
        tot=0
        while queue:
            length=len(queue)
            tot+=1
            for i in range(length):
                node=queue.popleft()
                if tot!=depth-1:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    newnode=TreeNode(val)
                    newnode.left=node.left
                    node.left=newnode
                    newnode2=TreeNode(val)
                    newnode2.right=node.right
                    node.right=newnode2
        return root
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
