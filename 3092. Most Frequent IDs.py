class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        n=len(nums)
        maxi=0
        dic={}
        lst=[]
        tot=0
        heap=[]
        for i in range(n):
            if nums[i] in dic:
                dic[nums[i]]+=freq[i]
            else:
                dic[nums[i]]=freq[i]
            if dic[nums[i]]!=0:
                heapq.heappush(heap,[-dic[nums[i]],nums[i]])
            tot+=freq[i]
            if tot==0:
                maxi=0
                lst.append(0)
            else:
                while heap and dic[heap[0][1]]!=abs(heap[0][0]):
                    heapq.heappop(heap)
                if heap:
                    lst.append(abs(heap[0][0]))
                else:
                    lst.append(0)
        return lst
''' Time Complexity--O(n*klogk)
    Space Complexity--O(n)'''
