class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l,r=0,len(letters)-1
        while l<=r:
            mid=(l+r)//2
            if letters[mid]>target and mid!=0 and letters[mid-1]>target:
                r-=1
            elif letters[mid]<=target:
                l+=1
            else:
                return letters[mid]
        return letters[0]
''' Time Complexity--O(logn)
    Space Complexity--O(1)'''
