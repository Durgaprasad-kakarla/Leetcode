class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        prev_u,prev_v=-1,-1
        for u,v in edges:
            if prev_u==-1 and prev_v==-1:
                prev_u=u
                prev_v=v
            elif prev_u==v:
                return v
            elif prev_v==u:
                return u
            elif prev_u==u:
                return u
            elif prev_v==v:
                return v
        return -1
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
