class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        list1 = [1] * n#firstly take an array with all one's in it with length 'n'
        #Using Sieve of Eratosthenes
        #we are taking the multiples of 2 to ceil(squareroot(n)) as '0' in the list as they are not primes 
        for i in range(2, int(math.sqrt(n))+1, 1):
            if list1[i] == 1:
                for j in range(i * i, n , i):
                    if list1[j]==1:
                        list1[j] = 0
        return sum(list1)-2

            
