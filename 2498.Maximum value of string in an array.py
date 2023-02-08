class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max1=0
        for i in strs:
            if i.isnumeric():
                if max1<int(i):
                    max1=int(i)
            else:
                if max1<len(i):
                    max1=len(i)
        return max1
