class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n=len(words)
        dic=dict(Counter(words[0]))
        for i in range(1,n):
            ch_count=dict(Counter(words[i]))
            for i in dic:
                if i in ch_count:
                    dic[i]=min(dic[i],ch_count[i])
                else:
                    dic[i]=-float('inf')
        characters=[]
        for i in dic:
            if dic[i]!=-float('inf'):
                for j in range(dic[i]):
                    characters.append(i)
        return characters
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
