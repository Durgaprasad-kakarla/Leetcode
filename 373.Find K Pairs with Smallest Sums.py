class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1=len(nums1)
        n2=len(nums2)
        pq = []
        for i in range(len(n1)):
            for j in range(len(n2)):
                total = nums1[i] + nums2[j]
                if len(pq) < k:
                    heapq.heappush(pq, (-total, [nums1[i], nums2[j]]))
                elif total < -pq[0][0]:
                    heapq.heappop(pq)
                    heapq.heappush(pq, (-total, [nums1[i], nums2[j]]))
                else:
                    break
        
        ans = []
        while pq:
            ans.append(pq[0][1])
            heapq.heappop(pq)
        
        return ans[::-1] 
''' Time Complexity--O(n1*n2*logk)
    Space Complexity--O(k)'''
