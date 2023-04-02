class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n=len(potions)
        list1=[]
        count=0
        for i in spells:
            count=0
            l=0
            r=n-1
            flag=0
            while l<=r:
                mid=(l+r)//2
                if potions[mid]*i>success:
                    r=mid-1
                elif potions[mid]*i<success:
                    l=mid+1
                else:
                    if mid==0 or potions[mid]*i!=potions[mid-1]*i:
                        flag=1
                        break
                    else:
                        r=mid-1
            if flag==0:
                list1.append(n-l)
            else:
                list1.append(n-mid)
        return list1
 '''Time Complexity--O(n*logn)
    Space Complexity--O(n)'''
