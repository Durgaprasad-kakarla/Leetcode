# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(node, x, y, columns):
            if node is None:
                return
            columns[x].append((y, node.val))
            traverse(node.left, x - 1, y + 1, columns)
            traverse(node.right, x + 1, y + 1, columns)

        columns = defaultdict(list)
        traverse(root, 0, 0, columns)

        result = []
        for x in sorted(columns.keys()):
            column = [val for y, val in sorted(columns[x])]
            result.append(column)

        return result


