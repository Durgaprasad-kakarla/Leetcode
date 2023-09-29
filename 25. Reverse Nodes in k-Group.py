# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k==1:
            return head
        dummy=ListNode(0)
        dummy.next=head
        curr,nex,pre=dummy,dummy,dummy
        cnt=0
        while curr.next:
            curr=curr.next
            cnt+=1
Comp            curr=pre.next
            nex=curr.next
            for i in range(1,k):
                curr.next=nex.next
                nex.next=pre.next
                pre.next=nex
                nex=curr.next
            pre=curr
            cnt-=k
        return dummy.next
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
