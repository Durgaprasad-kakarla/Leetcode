class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic={5:0,10:0}
        n=len(bills)
        for i in range(n):
            if bills[i]==5:
                dic[5]+=1
            elif bills[i]==10:
                if dic[5]>0:
                    dic[5]-=1
                else:
                    return False
                dic[10]+=1
            else:
                if dic[5]>0 and dic[10]>0:
                    dic[5]-=1
                    dic[10]-=1
                elif dic[5]>2:
                    dic[5]-=3
                else:
                    return False
        return True
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
