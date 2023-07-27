class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly=[1]
        x=len(primes)
        newlist=[0 for i in range(x)]
        while n>1:
            list2=[primes[i]*ugly[newlist[i]] for i in range(x)]
            min_ele=min(list2)
            for i in range(x):
                if min_ele==list2[i]:
                    newlist[i]+=1
            ugly.append(min_ele)
            n-=1
        return ugly[-1]
''' Time Complexity--O(n*x)
    Space Complexity--O(n)'''
