class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        st=str(n)
        lst=list(itertools.permutations(st))
        for ele in lst:
            ele="".join(ele)
            if ele[0]!='0':
                binary=bin(int(ele))[2:]
                if binary.count('1')==1:
                    return True
        return False
''' Time Complexity--O(n!)
    Space Complexity--O(n!)'''
