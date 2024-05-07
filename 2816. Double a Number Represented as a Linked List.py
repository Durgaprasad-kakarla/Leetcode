# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            dummy=None
            while head:
                curr=head.next
                head.next=dummy
                dummy=head
                head=curr
            return dummy
        l1=reverse(head)
        carry=0
        dummy=ListNode(None)
        temp=dummy
        while l1 or carry:
            sm=0
            if l1:
                sm+=l1.val*2
                l1=l1.next
            sm+=carry
            temp.next=ListNode(sm%10)
            temp=temp.next
            carry=sm//10
        return reverse(dummy.next)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
