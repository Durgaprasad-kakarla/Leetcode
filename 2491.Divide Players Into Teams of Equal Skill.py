class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total=0
        skill.sort()
        n=len(skill)
        l,r=1,n-2
        size=skill[0]+skill[-1]
        total=skill[0]*skill[-1]
        while l<r:
            if size==skill[l]+skill[r]:
                total+=(skill[l]*skill[r])
                l+=1
                r-=1
            else:
                return -1
        return total
''' Time Complexity--O(nlogn)
    Space Complexity--O(1)'''
