class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        list1=[]
        p=sorted(p)
        l=len(p)
        l1=len(s)
        if list(s)==p and len(s)==1:
            list1.append(0)
        for i in range(l1//2):
            if sorted(s[i:i+l])==p:
                list1.append(i)
            if l1-l-i>l1//2-1:
                if sorted(s[l1-l-i:l1-i])==p:
                    list1.append(l1-l-i)
        return list1
