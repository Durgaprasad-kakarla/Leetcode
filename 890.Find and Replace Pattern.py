class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        list1=[]
        for word in words:
            dict1={}
            dict2={}
            flag=0
            for j in range(len(word)):
                if pattern[j] in dict1:
                    if dict1[pattern[j]]==word[j]:
                        continue
                    else:
                        flag=1
                        break
                elif word[j] in dict2:
                    if dict2[word[j]]==pattern[j]:
                        continue
                    else:
                        flag=1
                        break
                else:
                    dict1[pattern[j]]=word[j]
                    dict2[word[j]]=pattern[j]
            if flag==0:
                list1.append(word)
        return list1
''' Time Complexity--O(n*len(word))
    Space Complexity--O(n)+O(2*len(word))''
