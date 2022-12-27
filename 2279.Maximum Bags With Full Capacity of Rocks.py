class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        list1=[]
        for i in range(len(capacity)):
            list1.append(capacity[i]-rocks[i])#append the difference of capacity and rocks of element at each 'i'
        list1.sort()#sort the list1 elements
        for i in range(len(list1)):
            if additionalRocks<0 or list1[i]>additionalRocks:#if list1[i] is greater than additionalRocks and additionalRocks is less than zero then break the loop
                break
            if list1[i]!=0 and additionalRocks>0:
                additionalRocks=additionalRocks-list1[i]#additionalRocks is replaced with additionalRocks-list1[i]
                list1[i]=0
        return list1.count(0)#Finally return the count of zero
