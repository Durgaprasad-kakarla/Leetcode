class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        dict1={}
        count1=0
        #Here we will store the length of the message of each sender in the dictionary(dict1)
        for s in messages:
            s=s.split(" ")
            if senders[count1] in dict1:
                dict1[senders[count1]]+=len(s)
            else:
                dict1[senders[count1]]=len(s)
            count1+=1
        list1=[]
        max1=max(dict1.values())
        #Here we will find the largest word count in the message and find the largest lexicographical sender if they are tied with same largest word count
        for key,value in sorted(dict1.items(),key=lambda x:x[1],reverse=True):
            if value==max1:
                list1.append(key)
            else:
                break
        return sorted(list1)[-1]
