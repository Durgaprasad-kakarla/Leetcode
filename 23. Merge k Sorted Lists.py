# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for head in lists:
            while head:
                heapq.heappush(heap,head.val)
                head=head.next
        dummy=ListNode(None)
        temp=dummy
        while heap:
            ele=heapq.heappop(heap)
            node=ListNode(ele)
            temp.next=node
            temp=temp.next
        return dummy.next
''' Time Complexity--O(n*len(list))
    Space Complexity--O(n*len(list))'''
