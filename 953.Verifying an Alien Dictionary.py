class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict1={" ":0}
        for i in range(len(order)):
            dict1[order[i]]=i+1#So dictionary contain the letters with their order
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            if len(w1)>len(w2):#It is used to avoid index out of range error
                w2=w2+" "*(len(w1)-len(w2))
            else:
                w1=w1+(" "*(len(w2)-len(w1)))
            print(w1,w2,len(w1),len(w2))
            for j in range(len(w1)):
                if w1[j]==w2[j]:#if they are having equal elements then continue the inner loop
                    continue
                elif dict1[w1[j]]<dict1[w2[j]]:#If they are sorted then break the loop and continue checking the next words in the list
                    break
                else:#If they are not sorted then return False
                    return False
        return True#If all are in sorted order then return True
