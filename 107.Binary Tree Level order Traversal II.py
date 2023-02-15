# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def func(root,list2,list1):
            if root is None:
                return
            queue = deque([root,None])
            while len(queue)>1:
                node = queue.popleft()
                if node is None:
                    queue.append(None)
                    list2.append(list1)
                    list1=[]
                    continue
                list1.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            list2.append(list1)
        list1=[]
        list2=[]
        func(root,list2,list1)
        return list2[::-1]
