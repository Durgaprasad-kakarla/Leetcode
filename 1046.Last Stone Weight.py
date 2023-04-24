class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            max1=max(stones)
            stones.remove(max1)
            max2=max(stones)
            if max1==max2:
                stones.remove(max2)
            else:
                stones.remove(max2)
                stones.append(max1-max2)
        return stones[0] if len(stones)==1 else 0
''' Time Complexity--O(n*n)
    Space Complexity--O(1)'''
