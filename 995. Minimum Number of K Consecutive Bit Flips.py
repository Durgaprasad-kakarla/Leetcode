class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        queue=deque()
        n=len(nums)
        res=0
        for i in range(n):
            while queue and i>queue[0]+k-1:
                queue.popleft()
            if (nums[i]+len(queue))%2==0:
                if i+k>n:
                    return -1
                res+=1
                queue.append(i)
        return res
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
