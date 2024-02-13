"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dic={}
        def dfs(node):
            if node in dic:
                return dic[node]
            copy=Node(node.val)
            dic[node]=copy
            for adj in node.neighbors:
                copy.neighbors.append(dfs(adj))
            return copy
        return dfs(node) if node else None
''' Time Complexity--O(V+E)
    Space Complexity--O(V)'''
