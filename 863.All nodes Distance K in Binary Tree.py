# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def distance(root,target,k):
            parent_dict = {}
            stack = [(root, None)]
            while stack:
                node, parent = stack.pop()
                if parent is not None:
                    print(node.val,parent.val)
                parent_dict[node] = parent
                if node.left:
                    stack.append((node.left, node))
                if node.right:
                    stack.append((node.right, node))
            list1=[]
            seen = set()
            queue = [(target, 0)]
            while queue:
                node, dist = queue.pop(0)
                if dist == k and node.val!=target.val:
                    list1.append(node.val)
                if k==0:
                    list1.append(node.val)
                elif dist < k:
                    if node.left and node.left not in seen:
                        queue.append((node.left, dist + 1))
                        seen.add(node.left)
                    if node.right and node.right not in seen:
                        queue.append((node.right, dist + 1))
                        seen.add(node.right)
                    if parent_dict[node] and parent_dict[node] not in seen:
                        queue.append((parent_dict[node], dist + 1))
                        seen.add(parent_dict[node])
            return list1
        return distance(root,target,k)
