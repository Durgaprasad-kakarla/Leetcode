class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split(" ")
        list1=[]
        if len(list(set(s)))!=len(list(set(pattern))):
            return False
        else:
            dict1=dict(zip(list(pattern),list(s)))
            print(dict1)
            for i in pattern:
                list1.append(dict1[i])
            if list1==list(s):
                return True
            else:
                return False
