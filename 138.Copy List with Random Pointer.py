"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        copyToRandom={None:None}
        while curr:
            copy=Node(curr.val)
            copyToRandom[curr]=copy
            curr=curr.next
        curr=head
        while curr:
            copy=copyToRandom[curr]
            copy.next=copyToRandom[curr.next]
            copy.random=copyToRandom[curr.random]
            curr=curr.next
        return copyToRandom[head]
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
