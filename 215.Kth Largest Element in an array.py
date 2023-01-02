class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]#using nlargest function of heapq module we can find the kth largest element in the array
