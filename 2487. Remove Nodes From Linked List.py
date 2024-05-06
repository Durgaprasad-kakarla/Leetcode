# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            dummy=None
            while head:
                curr=head.next
                head.next=dummy
                dummy=head
                head=curr
            return dummy
        head=reverse(head)
        maxi=head.val
        temp=head.next
        prev=head
        while temp:
            if temp.val>=maxi:
                maxi=temp.val
                prev.next=temp
                prev=prev.next
            else:
                prev.next=None
            temp=temp.next
        return reverse(head)
                        
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
