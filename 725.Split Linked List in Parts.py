# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr=head
        count=0
        while curr:
            curr=curr.next
            count+=1
        tot_list=[]
        curr=head
        if k>count:
            while curr:
                nxt=curr.next
                curr.next=None
                tot_list.append(curr)
                k-=1
                curr=nxt
            while k>0:
                tot_list.append(None)
                k-=1
        else:
            x=count//k
            modulo=count%k
            cnt=0
            tot_list.append(curr)
            while curr:
                cnt+=1
                if modulo>0 and cnt==x+1:
                    nxt=curr.next
                    curr.next=None
                    if nxt is not None:
                        tot_list.append(nxt)
                    modulo-=1
                    cnt=0
                    curr=nxt
                elif modulo==0 and cnt==x:
                    nxt=curr.next
                    curr.next=None
                    if nxt is not None:
                        tot_list.append(nxt)
                    cnt=0
                    curr=nxt
                else:
                    curr=curr.next
        return tot_list
''' Time Complexity--O(n)
    Space Complexity--O(k)'''
