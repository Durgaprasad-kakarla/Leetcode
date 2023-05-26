class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict1=defaultdict(int)
        dict1[0]=1
        presum=0
        count=0
        for i in range(len(nums)):
            presum+=nums[i]
            remove=presum-k
            count+=dict1[remove]
            dict1[presum]+=1
        return count
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
