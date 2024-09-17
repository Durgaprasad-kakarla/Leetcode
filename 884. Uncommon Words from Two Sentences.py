class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split(" ")
        s2=s2.split(" ")
        s=s1+s2
        dic=Counter(s)
        uncommon_words=[]
        for i in dic:
            if dic[i]<2:
                uncommon_words.append(i)
        return uncommon_words
''' Time Complexity--O(n1+n2)
    Space Complexity--O(n1+n2)'''
