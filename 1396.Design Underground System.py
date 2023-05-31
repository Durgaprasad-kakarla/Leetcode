class UndergroundSystem:

    def __init__(self):
        self.list1=[]
        self.checkout=[]
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.list1.append([id,stationName,t])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        for l in self.list1:
            if l[0]==id:
                self.checkout.append([l[1],stationName,abs(t-l[2])])
                self.list1.remove(l)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        x,c=0,0
        for station in self.checkout:
            if station[0]==startStation and station[1]==endStation:
                c+=1
                x+=station[2]
        return round(float(x/c),5)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
''' Time Complexity--O(n)
    Spacem complexity--O(n*3)'''
