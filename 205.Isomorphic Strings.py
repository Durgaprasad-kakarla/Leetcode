class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s))!=len(set(t)):
            return False
        else:
            dict1=dict(zip(list(s),list(t)))
            print(dict1)
            list1=[]
            for i in s:
                list1.append(dict1[i])
            print(list1)
            if list1==list(t):
                return True
            else:
                return False
