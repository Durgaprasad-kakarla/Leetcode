class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dict1={}
        #store the characters according to the indices elements
        for i in range(len(indices)):
            dict1[indices[i]]=s[i]
        s=""
        #After sorting the element of keys store it in the string
        for i in sorted(dict1.keys()):
            s=s+dict1[i]
        return s
