# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp=head
        prev=head
        #Iterate until temp is null
        while temp is not None:
            if temp.val==val:
              ## if the value present in the head itself then change the head to head.next
                if temp==head:
                    head=head.next
                    prev=head
                    temp=head
                # if it is not head then put the temp.next  in the prev.next then that node will be deleted
                else:
                    prev.next=temp.next
                    temp=temp.next
            #if it is not found then move the prev and temp to next 
            else:
                prev=temp
                temp=temp.next
        return head
