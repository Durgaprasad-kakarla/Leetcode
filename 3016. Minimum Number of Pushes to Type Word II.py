class Solution:
    def minimumPushes(self, s: str) -> int:
        def frequencySort(st):
            return "".join([char * times for char, times in collections.Counter(st).most_common()])    
        n=len(s)
        s=frequencySort(s)
        dic={}
        cnt=0
        for i in range(n):
            if len(dic)%8==0:
                x=2
            if s[i] not in dic:
                dic[s[i]]=[x,(len(dic)//8)+1]
                x+=1
            cnt+=dic[s[i]][1]
        return cnt
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
