class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        tot_observations=sum(rolls)
        remaining_observations=mean*(m+n)-tot_observations
        roll_dice=(remaining_observations)//n
        missing_observations=[]
        if roll_dice>6 or remaining_observations<0 or remaining_observations<n:
            return []
        elif roll_dice==6 and (remaining_observations)%n!=0:
            return []
        else:
            rem=(remaining_observations)%n
            while n>0:
                if rem>0:
                    missing_observations.append(roll_dice+1)
                    rem-=1
                else:
                    missing_observations.append(roll_dice)
                n-=1
            return missing_observations
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
