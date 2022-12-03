class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict1=Counter(words)
        dict2={}
        #creating a dictionary with count as keys and values as list of words
        for key,value in dict1.items():
            if value in dict2:
                dict2[value].append(key)
            else:
                dict2[value]=[key]
        list1=[]
        #Here we are storing the list of words which are having count in descending order and by maintaining lexicographical order of the words 
        for i in sorted(dict2.keys(),reverse=True):
            if len(list1)<k:
                list1=list1+sorted(dict2[i])
        return list1[:k]
