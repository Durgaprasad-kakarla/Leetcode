# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        if count==1:
            return None
        n1=count-n+1
        i=0
        temp=head
        prev=head
        while i<n1-1:
            prev=temp
            temp=temp.next
            i+=1
        if temp==head:
            head=head.next
        else:
            prev.next=temp.next
        return head
