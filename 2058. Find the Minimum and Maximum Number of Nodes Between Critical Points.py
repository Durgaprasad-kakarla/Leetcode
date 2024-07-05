# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        temp,prev,cnt,first,pre,mini=head,head,1,-1,-1,,float('inf')
        temp=temp.next
        while temp:
            if (temp.val>prev.val and temp.next and temp.val>temp.next.val) or (temp.val<prev.val
            and temp.next and temp.val<temp.next.val):
                if first==-1:
                    first=cnt
                    pre=first
                else:
                    mini=min(mini,cnt-pre)
                    pre=cnt
            cnt+=1
            prev=temp
            temp=temp.next
        return [-1,-1] if mini==float('inf') else [mini,pre-first]

''' Time Complexity--O(n)
    Space Complexity--O(1)'''
