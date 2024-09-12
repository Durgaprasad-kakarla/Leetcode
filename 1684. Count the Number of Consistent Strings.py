class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        word=set(allowed)
        cnt=0
        for s in words:
            flag=0
            for i in set(s):
                if i not in word:
                    flag=1
                    break
            if flag==0:
                cnt+=1
        return cnt
''' Time Complexity--O(n*len(s))
    Space Complexity--O(1)'''
