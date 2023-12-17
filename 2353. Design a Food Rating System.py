class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n=len(foods)
        self.dic3={}
        for i in range(n):
            if cuisines[i] not in self.dic3:
                self.dic3[cuisines[i]]=[]
        
        for i in range(n):
            heapq.heappush(self.dic3[cuisines[i]],[-ratings[i],foods[i]])
        self.dic2={}
        for i in range(n):
            if foods[i] not in self.dic2:
                self.dic2[foods[i]]=-ratings[i]
            else:
                self.dic2[foods[i]]=-ratings[i]
        self.dic4={}
        for i in range(n):
            if foods[i] not in self.dic2:
                self.dic4[foods[i]]=cuisines[i]
            else:
                self.dic4[foods[i]]=cuisines[i]
    def changeRating(self, food: str, newRating: int) -> None:
        self.dic2[food]=-newRating
        heapq.heappush(self.dic3[self.dic4[food]],[-newRating,food])

    def highestRated(self, cuisine: str) -> str:
        heap=self.dic3[cuisine]
        top=heap[0]
        while heap and  top[0]!=self.dic2[top[1]]:
            heapq.heappop(heap)
            if heap:
                top=heap[0]
        return top[1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
''' Time Complexity--O(n*logk)
    Space Complexity--O(n*k)'''
