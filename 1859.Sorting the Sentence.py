class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split(" ")#split the string which has space in between two strings
        list1=[]
        for i in s:
            i=list(i)
            #swap the last and first element of the array
            #if "This2" then "2This",so we can sort it easily 
            i[0],i[-1]=i[-1],i[0]
            #store these strings in the list1
            list1.append("".join(i))
        list1.sort()
        st=''
        for i in list1:
            i=list(i)
            ''' Now swap the elements at begin and end of the array,remove the last element i.e., integer '''
            i[0],i[-1]=i[-1],i[0]
            i.remove(i[-1])
            t="".join(i)
            st=st+t+" "
        return st[0:len(st)-1]#To avoid the last space slicing is used 
