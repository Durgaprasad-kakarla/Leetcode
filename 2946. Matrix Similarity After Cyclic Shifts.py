class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for lst in mat:
            n=len(lst)
            for i in range(n):
                if lst[i]!=lst[(i+k)%n]:
                    return False
        return True
''' Time Complexity--O(n*m)
    Space Complexity--O(1)'''
