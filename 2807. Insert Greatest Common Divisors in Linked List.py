# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        prev=temp
        temp=temp.next
        while temp:
            gcd=math.gcd(prev.val,temp.val)
            new_node=ListNode(gcd)
            prev.next=new_node
            new_node.next=temp
            prev=temp
            temp=temp.next
        return head
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
