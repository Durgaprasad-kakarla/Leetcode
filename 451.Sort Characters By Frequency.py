class Solution:
    def frequencySort(self, s: str) -> str:
        dict1=Counter(s)
        dict2={}
        st=''
        ##Here we are creating the dictionary with count as freqency and the values as the list of character which are having the same count 
        for key,value in dict1.items():
            if value in dict2:
                dict2[value].append(key)
            else:
                dict2[value]=[key]
        #now we have to store the characters with descending order of their count that's why have given reverse=True
        for i in sorted(dict2.keys(),reverse=True):
            j=0
            while j<len(dict2[i]):
                st=st+dict2[i][j]*i
                j+=1
        return st

