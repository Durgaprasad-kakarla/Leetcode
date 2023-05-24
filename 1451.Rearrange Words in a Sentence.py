class Solution:
    def arrangeWords(self, text: str) -> str:
        dict1={}
        text=text.split(" ")
        for i in text:
            if len(i) in dict1:
                dict1[len(i)].append(i)
            else:
                dict1[len(i)]=[i]
        s=""
        for i in sorted(dict1.keys()):
            for j in dict1[i]:
                s+=j+' '
        return s[0].capitalize()+s[1:len(s)-1].lower()
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
