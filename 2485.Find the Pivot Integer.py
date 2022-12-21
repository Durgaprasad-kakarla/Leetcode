class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        for i in range(n//2,n+1):#Starting from the middle
            if (i*(i+1))//2 ==(n*(n+1))//2-(i*(i+1))//2+i:#Finding the sum upto i and finding the sum from i to n.Check if they are equal return i
                return i
        return -1
      
