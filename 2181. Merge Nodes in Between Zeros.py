# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        temp=temp.next
        new_head,prev,sm=None,None,0
        while temp:
            if temp.val!=0:
                sm+=temp.val
            else:
                if not new_head:
                    new_head=ListNode(sm)
                    prev=new_head
                else:
                    prev.next=ListNode(sm)
                    prev=prev.next
                sm=0
            temp=temp.next
        return new_head
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
