class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a, int(''.join(map(str, b))), 1337)
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
