class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime=sorted(processorTime,reverse=True)
        tasks.sort()
        mini_time=0
        x=0
        for i in processorTime:
            maxi=i+max(tasks[x],tasks[x+1],tasks[x+2],tasks[x+3])
            x+=4
            mini_time=max(mini_time,maxi)
        return mini_time
''' Time Complexity--O(nlogn)--n->len(tasks)
    Space Complexity--O(1)'''
