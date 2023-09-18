class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n=len(mat)
        my_dict={}
        for i in range(n):
            my_dict[i]=sum(mat[i])
        sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
        return list(sorted_dict)[:k]
''' Time Complexity--O(n*n)
    Space Complexity--O(n)'''
